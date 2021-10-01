import requests


BASE_URL = "http://127.0.0.1:5000/"
VIDEO_URL = BASE_URL + "video/%d/"


data = [
    {"name": "video-01", "views": 5, "likes": 100000},
    {"name": "video-02", "views": 500, "likes": 20},
    {"name": "video-03", "views": 10, "likes": 2}
    ]

# for i in range(len(data)):
#     res = requests.put(f"http://127.0.0.1:5000/video/{i}/", data[i])
#     print("put==>", res.json())


# res = requests.patch("http://127.0.0.1:5000/video/2/", {"views": 100})
# print("patch==>", res.json())

res = requests.patch("http://127.0.0.1:5000/video/2/")
print("delete==>", res.json())

res = requests.get("http://127.0.0.1:5000/video/2/")
print("get==>", res.json())
