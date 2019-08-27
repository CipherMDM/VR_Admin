from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials,firestore
import json




# Create your views here.

json_data = {
  "type": "service_account",
  "project_id": "chatz-2017",
  "private_key_id": "9b1c8b85f6d7568e8bd515446e56303e78b8c37a",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDawwj4t/ixKMrg\nEkLFeVYDX7PDIm/gPluxeHIVDABFQwMl2aYypsd7dUh84zqBdq640S4R6xWEtTpC\n3xockDyOLUAw0y9BMypQxjCZ8b5khFFNUNpnpwcmhpBwBvGfDVsRQijhI6wPPMfH\nKtgzSHRAamdAzjvGGmCxLHNF/XILo5A+I63DLDRfpd9ccs3JrbBb8CBgdUwXrVYv\neSfc+VAOwUSmvysKhZbMca/w7+FpnRa2jzWX47SvsjKOPexJBlDsVxD4AG4M2Ibn\nQf4ZTDg+K/9i2hUU3NRf+fOWmf/N9/nnK1DWTB3fzj+aE0zGvQ4GdTdDEU7aq9Eh\nnrSeHEtvAgMBAAECggEAFSeOGwsjU/JnZ/KsHU+F906OYhzW577v/AHzOkDOV+RK\njiL1dOl22eP2DgmlMzbIX5vu0hHDI3GpACV173QtPux2TCJn6+yoN2Zq9cAQUsUO\n3aSnciWPRfT2S7cIL4LJnyogLOFXtqOAiCyG+rKTd1UyxewLkLUlS4zKWubO2/wX\n5IyExNR7iMcUJNOzR2vVNu1OgGLFUfKnKXAI1xxf6sporyJUu8y1kdGR4UFU1kbc\nAa0QIJ8jJ3nm6/p2Y67VDI4H7tWafi1jBlWbsrb0nW/4I1SYMCAkp4Ti0P4KkNgk\nocB93jaTXk954nMCiPNvWqk/3T5jJ4vfG3Ng5dSyNQKBgQDw0B9GMnRO7g9aJTG6\naNcvc/mr6SToON0cDaJnbFnBcfK+vAFnm5ZDsgwGKhuXurwRUCj/yZ2RoWN7ZOau\nG+lJ/1TJjA2q5M/QQfLp2MR5Ot6KPXpCJ+AMuA0bgDaGjsazMBahK4XmQOWbK1EM\n9zZL0zA6BeFE2gMsBwIv7kgczQKBgQDojubiMFjfrU6ADJVvbrBOGXxI5JHxKVJ0\nVkNSIw6kCP17kwD8M9cNhcKP/es1PTigEatFwQ3ljPt3cav5wyZUH8091VswZFPh\nIb0cwyO8fhkvIVh92JhT5ia3QGy95uG4Y7OdCXYSQqybteClkOAzKNfxfAgDI2B0\nLFhb1u1JKwKBgHzEJ9/z1iTq3JNk/+3H0e2pFeuGwPN8OrsFKWaSUbKTOiSuPcAT\ncXgjcG1lNaSYQEZsFMHqELRaPLO65HXCykzneGNwJ8iqAi2xbYzRHYJ+CLzw+z35\ncPDGDyx3ckinArXmLWNVrGtOpmeNutGP59bDVZJKZ5uHpOsTuoNg3oXlAoGBAIui\nMfMhwFsdPgMYiylLNsTN/Jfv1ckNXJrJqMZKkmHfnAN0sqS7o6ZU6At5FJ700Wka\n8tGBJwzrZ5nCQNZIXF0qcxtrXcNimhKVJW19pZlpxUlNJkr5oAzQJfLl1eT4GhOS\nmafypFg2fFlKDUacBGHzZiVyqYTo2uMmNS9/jx3dAoGAJCOV3aoGFy8CGR7mywLu\nDm5osNWDn6FF5M4DvA3erL52F2rgTpjphV1X3fvt5IAAuadWsyU0Z404m9HrYYX2\nqrWJVmOjLkAy+OdbHa8EYZBlXNQMKnotzj85Zy/QyuNpfG4+TpF0r4jE8gR3chPt\nSNV335tLS0PRkWE/8tt8SZ8=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-b71zc@chatz-2017.iam.gserviceaccount.com",
  "client_id": "112497572942775837109",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-b71zc%40chatz-2017.iam.gserviceaccount.com"
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
    db.collection("Informations").document(i.id).update({"Message":request.POST["ping"]})
    
  return render(request,"index.html",{"data":data})  





