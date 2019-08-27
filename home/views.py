from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials,firestore
import json




# Create your views here.

json_data = {
  "type": "service_account",
  "project_id": "project-vr-f4bf3",
  "private_key_id": "748e45d303a90d79dc8ed24259937baa2b8e9ac1",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCuK19OFA/xl70x\nrSIv9iGSiBCCJjowxOf3ECB3+DnxFViLL+b7FBCvawNjjYjbqNBpnI6NtjI94n2/\nxuANf3I1Sf94qI1ZmL7MrXoRJJ9mw1CULLi1CXVZNgcYr42AUaWeV12+WYJH8Tt/\nTrpoNRk7Fj19tuKy4Obrg6CKwDBwRNJTalPRoLLr1fybG4NN31zt0Nvg0SDDvY+y\nCrhGd1u1yZQmtSiA2PyLMm19aYn8TMBl2u3l7LdxbnHaAyxPRHcdIPMK5lgM3FHA\nAVDxfqwAFZGE00XGewuRlhpxH0p7Pv2S93ufY+jt2JxjMQoah521d9LCBZC7V9r0\ngFIYHtG/AgMBAAECggEANvQMYBBIb4vW8AOWk9dvBFLWEpqJJbYbEoMOG4xAi+aW\nR2RX1sSf9xkmupR/p/79szTobaIc/BWoY4gWTWv21wWAC8vyvWBKYz4hE6Ogf8YE\neJwbs1NGqV04o/tQBDq+rNUYCOUpDBX7FdH7UsHeMhx0TmQT5yi683hWgTDel604\n5oUrY1F0JfsAkWRdmK2ixqol4LKQI5LtgLL6v8DLOhH6/pEELsZNz0ccWupW2U55\n0FobvHJ5qTU+BlDPCDKYZd6Q+5JpzYvI2w56IQNj11Y1Tlf/+cIGBhI3oJoKQSYH\njQy/9xVlh4yWvpomUkdfCJR7EZAG2WHruESfyg9AYQKBgQDwgIUyjUAhRmjTr7Vo\n16eV0qOhaGhVPH9CzJE+UHmBvuAaePj3N/FXqwityCwAXKDjsVgj85/AHIbp7tm9\n/zmnXPK5vXliREfOXxB4F1KODHBliC9b7DwO9EoBmPbKGS6Ii/OmQkrAMJWxuBJl\nH/rbTvPpSRay3/Of2ORJCOJcGQKBgQC5ZJXsAEAW8IkunA3k0T9WJP7FUUHiwIa2\nO4+rM2D7FWCcNoM73DMhxfrOqb4sAhpnhxN9IdaiQhM+L9y7CInGzm5E3SshHXbx\nrULjmsqGW7alFY7c7jP+6n90TMjqOFB6u9aIofDRBobOgDkm0W0fsvUShmOoSEd4\nXP9/gX5XlwKBgQChl5jnaGTIdsiEQzD+qredQRRUpRRFAQr41P5aAjRB6wAkiVeu\ns9Xi87Y3HaIC9DneAxCXx1908zXrBGMk99HDE/66sgZW8k3U6ablKbZ8Xvs+HQzF\nFKsd2SHIhQB8tgLAGFizQyN6kqph6K3jaGNi61+TRVqNAVBt/IsWT3PYMQKBgE4Z\nKW75zAXd3mxcIR47Z8sKWqkUygSTxiwOez9LrZcYMlKcRDx7Tq7zj+xvZUV0vVrP\ndE5Kavh/jUutLfc8aY3ueFVaNkkE+I5mxr7K/nYLPK3enwhC8HR6pKaBkkHY505M\nwttcHO5xKWjkay8HGkk4QjVDl8fUawcxZhB4pJiRAoGAdcBaPJ96JQuHhwFvbrwJ\n2Op8zhKznPbEqViSqgQ97JbJ3YBtfVwGkMDsP6UDuJ9alMZiPPQRz9IrjkQ8yqqi\nCdCytQZy2166czjKxNioAfBSrkFvPqnxBuQAmXKnWBdM8l7rDQRh1YKF+8I19+7l\n78Y/mNAPutF3MeUnO8GmwmI=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-zgl3m@project-vr-f4bf3.iam.gserviceaccount.com",
  "client_id": "105547683581945093939",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-zgl3m%40project-vr-f4bf3.iam.gserviceaccount.com"
}

cred = credentials.Certificate(json.loads(json.dumps(json_data)))
firebase_admin.initialize_app(cred)

def home(request):
   
    db = firestore.client()  
    
    data = []
    for i in db.collection("Informations").get():
        data.append(i.to_dict())
    return render(request,"index.html",{"data":data})
def ping(request):
  db = firestore.client()
  data = []
  print(request.POST["btn"])
  doc = db.collection("Informations").where("Device_info.id","==",request.POST["btn"]).get()
  for i in doc:
    data.append(i.to_dict())
    db.collection("Informations").document(i.id).update({"Status":request.POST["ping"]})
    
  return render(request,"index.html",{"data":data})  





