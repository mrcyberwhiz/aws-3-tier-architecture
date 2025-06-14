# Three-Tier Architecture Project Steps

![Architecture Diagram](AWS_3-Tier_Architecture.png)

## 1. Create a VPC

## 2. Create 6 Subnets

- 2 Subnets for Web Server
- 2 Subnets for App Server
- 2 Subnets for Database

## 3. Create Route Tables

- **Public Route Table**: Connects with Internet Gateway and 2 public subnets.
- **Private Route Table**: Create Private Route table for eachsubnet and Map NatGateway from each Availability zone for High Availability
- **No NAT for Database**: If required for database patching, Map Natgateway to Database Route table

## 4. Create 5 Security Groups

- **InternetFacingApplicationloadbalancerSG**: Allows SSH (ALL) , HTTP (ALL), HTTPS (ALL).
- **WebServerEC2SG**: Allows SSH (ALL), HTTP (ALL), HTTPS (ALL).
- **InternalApplicationLoadbalancerSG**: Allows SSH (ALL) , HTTP (ALL), HTTPS (ALL).
- **AppServerEC2SG**: Allows 5000 from InternalApplicationLoadbalancerSG, SSH from InternalApplicationLoadbalancerSG, 80 from InternalApplicationLoadbalancerSG, 443 from InternalApplicationLoadbalancerSG.
- **DatabaseSG**: Allows 3306 from AppServerEC2SG.

## 5. Create Route 53 (R53) Hosted Zone

- Create a Hosted Zone for a domain name.
- Map R53 NameServer with your Domain Service Provider.

## 6. Validate ACM with R53

- Request a Certificate for your domain name.
- Create a CNAME record in R53 from ACM to validate your domain ownership.

## 7. Create RDS

- Create a DB Subnet group *at least 2 subnets needed*.
- Create a MySQL DB in a private subnet with threetasubnetgroup.

## 8. Create Web Server EC2

- Launch an EC2 instance in the public subnet with WebServerEC2.

## 9. Create App Server EC2

- Launch an EC2 instance in the private subnet with AppServerEC2.

## 10. Command to Login to App Server

```bash
vi 3TA.pem
chmod 400 3TA.pem
ssh -i 3TA.pem ec2-user@<AppServer ip>
```

## 11. Setup Database

```bash
sudo yum install mysql -y
mysql -h <database_endpoint> -P 3306 -u admin -p
```

- Provide queries from **commands.sql** file to create DB, tables, and insert data into the table.

## 12. Setup App Server

```bash
sudo yum install python3 python3-pip -y
pip3 install flask flask-mysql-connector flask-cors
vi app.py

nohup python3 app.py > output.log 2>&1 &
ps -ef | grep app.py

cat output.log 
curl http://10.0.3.47:5000/login
```

## 13. Setup Web Server

```bash
sudo yum install httpd -y
sudo service httpd start
cd /var/www/html/
touch index.html script.js styles.css
```
- Move the Front-End files.

## 14. Create Application Load Balancer (ALB)

- Create **Frontend Target Group** for Web Server EC2 with:
  - Port: 80
  - Health Check Path: `/index.html`
- Create **Frontend Load Balancer** in the public subnet with:
  - Listener Port: 80
  - Attach the Target Group

## 15. Create Application Load Balancer (ALB)

- Create **Backend Target Group** for App Server EC2 with:
  - Port: 5000
  - Health Check Path: ` /booksawindex.html`
- Create **Backend Load Balancer** in the public subnet with:
  - Listener Port: 80
  - Attach the Target Group

## 16. Configure Route 53 to Load Balancer

- Create an **A record** with alias pointing to the Frontend Load Balancer.

## 17. Attach ACM Certificate to Load Balancer

---
