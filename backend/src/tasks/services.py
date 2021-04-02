from django.conf import settings
from rest_framework.response import Response

from src.tasks.client import RestClient
from src.tasks.models import Task, TaskData, TaskResult

from src.tasks.serializers import TaskCreateSerializer

client = RestClient(settings.SERP_LOGIN, settings.SERP_PASSWORD)


def task_post(self, request):
    serializer = TaskCreateSerializer(data=request.data)
    if serializer.is_valid():

        post_data = dict()
        post_data[len(post_data)] = dict(
            language_code="en",
            location_code=serializer.data['location'],
            keyword=serializer.data['keyword'],
        )

        response = client.post(f"/v3/serp/{serializer.data['engine']}/organic/task_post", post_data)

        if (
                response["status_code"] == 20000
                and response["tasks"][0]["status_code"] == 20100
        ):
            res = response["tasks"][0]

            task = Task.objects.create(
                id=res["id"],
                status_code=res["status_code"],
                status_message=res["status_message"],
                time=res["time"],
                cost=res["cost"],
            )
            TaskData.objects.create(task=task, **res["data"])
        else:
            error = f"error. Code: {response['status_code']} Message: {response['status_message']}"
            return Response(status=400, data=error)
    return Response(status=201)


def tasks_ready(self):
    results = Task.objects.all()
    tasks = [task for task in results if task.status_message == "Task Created."]

    for task in tasks:

        response = client.get(f"/v3/serp/{task.data.se}/organic/tasks_ready")

        if response["status_code"] == 20000:
            for resp_task in response["tasks"]:
                if resp_task["result"]:
                    for result in resp_task["result"]:

                        Task.objects.filter(id=result["id"]).update(
                            status_code=resp_task["status_code"],
                            status_message=resp_task["status_message"],
                        )
        else:
            error = f"error. Code: {response['status_code']} Message: {response['status_message']}"
            return Response(status=400, data=error)

    results = Task.objects.all() if tasks else results
    return Response(status=200, data=results)


def task_get(self):
    pk = self.kwargs["pk"]
    engine = self.kwargs["se"]

    task_id = Task.objects.filter(id=pk).first()
    results = []

    if task_id.status_message == "Downloaded":
        results = TaskResult.objects.filter(task=task_id)
        return results

    response = client.get(f"/v3/serp/{engine}/organic/task_get/regular/{pk}")

    if response["status_code"] == 20000:
        task = response["tasks"][0]

        if task["result"] and (len(task["result"]) > 0):
            for result in task["result"]:
                res = []

                if result["items"]:
                    for item in result["items"]:
                        item["task"] = task_id
                        res.append(item)

                    TaskResult.objects.bulk_create([TaskResult(**i) for i in res])
                    Task.objects.filter(id=pk).update(status_message="Downloaded")
                else:
                    Task.objects.filter(id=pk).update(status_message="No Search Results.")
                    return

        results = TaskResult.objects.filter(task=task_id)
    return results