# Server Commands Reference

Quick copy-paste commands for the training sessions.

---

## Session 3: Compute

### Update System & Install Nginx
```bash
apt update
apt upgrade -y
apt install nginx -y
systemctl start nginx
systemctl enable nginx
systemctl status nginx
```

### Configure UFW Firewall
```bash
ufw allow 'Nginx HTTP'
ufw enable
ufw status
```

### Create Custom Webpage
```bash
cat > /var/www/html/index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>My First Cloud Server</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        h1 { color: #0080ff; }
        .info {
            background: #e8f4f8;
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to Digital Ocean!</h1>
        <p>This webpage is hosted on a Droplet.</p>
        <div class="info">
            <strong>Server Details:</strong>
            <ul>
                <li>Platform: Digital Ocean Droplet</li>
                <li>Web Server: Nginx</li>
                <li>OS: Ubuntu 22.04 LTS</li>
            </ul>
        </div>
    </div>
</body>
</html>
EOF
```

---

## Session 3: Object Storage

### Install Python & Boto3
```bash
apt install python3 python3-pip -y
pip3 install boto3
```

### Create Backup Script
```bash
nano /root/backup_to_spaces.py
```

Paste the content from `backup_to_spaces.py`, then update:
- Line 12: `SPACES_KEY = 'YOUR_ACCESS_KEY'`
- Line 13: `SPACES_SECRET = 'YOUR_SECRET_KEY'`
- Line 14: `SPACES_REGION = 'sgp1'`
- Line 15: `SPACES_BUCKET = 'your-bucket-name'`

### Run Backup Script
```bash
chmod +x /root/backup_to_spaces.py
python3 /root/backup_to_spaces.py
```

### Schedule Daily Backup (Cron)
```bash
crontab -e
```

Add this line for 2 AM daily backup:
```
0 2 * * * /usr/bin/python3 /root/backup_to_spaces.py >> /var/log/backup.log 2>&1
```

---

## Session 5: Networking

### Web Server Setup (Run on web-server-01 and web-server-02)
```bash
apt update && apt install nginx -y

cat > /var/www/html/index.html << EOF
<!DOCTYPE html>
<html>
<head><title>Web Server</title></head>
<body>
    <h1>Hello from $(hostname)</h1>
    <p>Private IP: $(hostname -I | awk '{print $1}')</p>
    <p>Timestamp: $(date)</p>
</body>
</html>
EOF

systemctl enable nginx
systemctl start nginx
```

### Test Private Connectivity (from web-server to db-server)
```bash
# Replace with actual private IP from Control Panel
ping 10.110.0.X
```

### Install MySQL Client (Optional)
```bash
apt install mysql-client -y
mysql -h 10.110.0.X -u root -p
```

### Test Load Balancer Failover
```bash
# Stop nginx to simulate failure
systemctl stop nginx

# Start nginx to recover
systemctl start nginx
```

---

## Useful Commands

### Check Server Info
```bash
hostname
hostname -I
cat /etc/os-release
free -h
df -h
```

### Nginx Management
```bash
systemctl status nginx
systemctl restart nginx
systemctl reload nginx
nginx -t  # Test config
```

### View Logs
```bash
tail -f /var/log/nginx/access.log
tail -f /var/log/nginx/error.log
```

### Check Open Ports
```bash
ss -tlnp
```
