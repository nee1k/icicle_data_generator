## 1. Build the Docker Image
```bash
sudo docker build -t data_generator .
```

## 2. Create a Docker Volume
```bash
sudo docker volume create icicle
```

## 3. Run the Container
```bash
sudo docker run --rm -v icicle:/data data_generator python /usr/src/app/log_accuracy.py
```

## 4. Verify Output
```bash
sudo docker run --rm -v icicle:/data alpine ls /data
```
```bash
sudo docker run --rm -v icicle:/data alpine cat /data/acc.json
```