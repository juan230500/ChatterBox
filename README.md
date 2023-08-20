
# ChatterBox: Simple AWS Cloud Chatbot

A simple chatbot implemented using AWS Lambda, API Gateway, and hosted on an EC2 instance.

## Step 1: Create a Lambda Function on AWS

1. Navigate to Lambda in AWS Console.
2. Create function -> Author from scratch.
3. Name the function (e.g., `chatbotFunction`).
4. Choose Python 3.8 as runtime.
5. Use the code from `lambda_function.py`.

## Step 2: Configure API Gateway

1. Navigate to API Gateway.
2. Create API -> HTTP API.
3. Connect to the Lambda function created earlier.
4. Define resource and GET method.
5. Set up CORS to allow all origins (`*`).
6. Define the endpoint as `/chatbotFunction`.
7. Deploy the API.
8. Take note of the URL.

## Step 3: Create and Host the Web Page on EC2

### Create an EC2 Instance:

1. Go to EC2 in AWS Console.
2. Launch Instance.
3. Select AMI (Amazon Linux 2).
4. Choose instance type (t2.micro).
5. Set up a security group (allow HTTP traffic on port 80).
6. Launch the instance.

### Connect and Configure EC2 Instance:

1. Connect via SSH.
2. Install web server:

```bash
sudo yum install httpd -y
sudo service httpd start
```

3. Navigate to the web pages directory:

```bash
cd /var/www/html
```

4. Use `nano` to create and edit `index.html`:

```bash
sudo nano index.html
```

5. Paste the code for `index.html`.

6. **Note**: In `index.html`, replace `YOUR_API_URL` with the full URL of your API Gateway (including the endpoint `/chatbotFunction`).

# Files in the Repository

- `lambda_function.py`: Code for the Lambda function.
- `index.html`: HTML code for the web page.