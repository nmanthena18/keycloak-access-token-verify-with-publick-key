from flask import Flask
import jwt
import requests
from keycloak.keycloak_openid import KeycloakOpenID
import jwt
from jwt.algorithms import RSAAlgorithm
app = Flask(__name__)

@app.route("/")
def hello_world():
    # Fetch the public key
    public_key_url = "<https://your-keycloak-server-url>/realms/<remal>/protocol/openid-connect/certs"
    public_key_response = requests.get(public_key_url)

    public_key = public_key_response.json()["keys"][0]

    public_key2 = RSAAlgorithm.from_jwk(public_key)

    # Your access token
    access_token = "<your access token>"
    # Verify the token
    try:
        print("intry")
        # decoded_token = jwt.decode(access_token, public_key, algorithms=["RS256"])eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJlQW5oYTB0WFhJbHh0bGlGOUc1QmN1bUFIS0s2MWxIZHVTYjZxd3V2d1ZJIn0.eyJleHAiOjE2OTMzMDQ3NjUsImlhdCI6MTY5MzMwNDQ2NSwiYXV0aF90aW1lIjoxNjkzMzA0NDY0LCJqdGkiOiI0OTJmYjhhNi02OTZiLTQ1YmEtODI0NS00MWZmMDQyYmYwMWYiLCJpc3MiOiJodHRwczovL2lkcC5pbnRlbGxhaXJlLmNvbS9yZWFsbXMvdGVzdGluZyIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI2ZWM5MGVmMS0xNzA4LTQyNmUtOTAxZC0wNjg0YmNiMjE5ZjkiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJkYXNoYm9hcmQiLCJzZXNzaW9uX3N0YXRlIjoiMDAxYzllYWQtNWY3ZC00NDhkLWJjZGUtYTQwYjU2NGFmM2UyIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyJodHRwOi8vbG9jYWxob3N0OioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbImRlZmF1bHQtcm9sZXMtdGVzdGluZyIsIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX0sImRhc2hib2FyZCI6eyJyb2xlcyI6WyJkYXNoYm9hcmQtdXNlciIsImRhc2hib2FyZC1hZG1pbiIsImRhc2hib2FyZC10ZXN0LXJvbGUiXX19LCJzY29wZSI6Im9wZW5pZCB0ZXN0LWNsaWVudC1zY29wZSBwcm9maWxlIGVtYWlsIiwic2lkIjoiMDAxYzllYWQtNWY3ZC00NDhkLWJjZGUtYTQwYjU2NGFmM2UyIiwidXNlcnJlYWxtcm9sZSI6IltkZWZhdWx0LXJvbGVzLXRlc3RpbmcsIG9mZmxpbmVfYWNjZXNzLCB1bWFfYXV0aG9yaXphdGlvbl0iLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsImFkZHJlc3MiOnt9LCJuYW1lIjoidXNlciB1IiwibmFyZXNoIjoiW2Rhc2hib2FyZC11c2VyLCBkYXNoYm9hcmQtYWRtaW4sIGRhc2hib2FyZC10ZXN0LXJvbGVdIiwicHJlZmVycmVkX3VzZXJuYW1lIjoidXNlciIsImdpdmVuX25hbWUiOiJ1c2VyIiwiZmFtaWx5X25hbWUiOiJ1In0.QyzvadDXZOauC9rGBkRzKvjNARd5icdtSxotB1de5WCP8c_Ct7cHyjobnilZzrmJbnMPPIdnrv5QAd__GyUp4u08t9BsvMgxni7Sb_s5FA-bMNDSJTAt2NYA6fpIAIjialZTD7XyObvCSTAhc3oCg-DlSKDOX-XXZrjqYIOoPhB9gnPwrtb1WgMERJ6iT1pTL2INbaJYzApEe3UHbHe-QQtLJaDnm-_Qo-yPBvZGE4CAfLwGNS9_RNkoXBbiHYIuYfPfEhqwopeHvQWl4KQ7_iuLwG01pFvrAKhYtYdn_NJkefuRoUWQ3DT48OjUZ7zyNhggFCggu9j6EAnC0nk4kA
        decoded_token = jwt.decode(
                  access_token,
                  public_key2,
                  algorithms=['RS256'], audience='account'
              )
        # Validate claims (e.g., exp, iss)
        # Implement your custom validation logic here
        print("Token is valid!", decoded_token)
    except jwt.ExpiredSignatureError:
        print("exception")
        print("Token has expired.")
    except jwt.InvalidTokenError:
        print("Token is invalid.")



    return "<p>Hello, World!</p>"

