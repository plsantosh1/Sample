---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flaskapp
  labels:
    app: flaskapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: flaskapp
  template:
    metadata:
      labels:
        app: flaskapp
    spec:
      containers:
      - name: flaskapp
        image: gcr.io/GCP_PROJECT_ID/flaskapp:VERSION
        ports:
        - containerPort: 8080

---
kind: Service
apiVersion: v1
metadata:
  name: flaskapp
spec:
  selector:
    app: flaskapp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
  type: LoadBalancer
