# SMS sending tool

This repo includes a simple rest API without authentication for sending an SMS via Twilio.

## Requirements

- Docker
- Front-end client framework of your choice, we use Angular

## Build the docker api image

```sh
docker build -t sms-tool:latest .
```

## Run the image locally

Runs the Flask app and exposes it on localhost port 5000. Insert the credentials provided for this exercise into the following command.

```sh
docker run -it --rm -e TWILIO_ACCOUNT_SID="INSERT ACCOUNT SID" -e TWILIO_ACCOUNT_TOKEN="INSERT TOKEN" -e TWILIO_PHONE_NUMBER="INSERT PHONE NUMBER" -p 5000:5000 sms-tool
```

## Hit the api

You should now be able to hit the docker container from your client using the following endpoint "http://localhost:5000/sms/send"
The endpoint expects 2 parameters:

- "to": a valid phone number string (UK only please)
- "message": the text message body content string

```json
{
  "to": "441234567890",
  "message": "Some message to someone\nFrom\nConsultant Connect"
}
```
