docker run --gpus all -it --rm ^
  -p 8888:8888 ^
  -v "D:\0.LatestDSCourse\DS_course\TransferLearning:/tf/code" ^
  tensorflow/tensorflow:2.14.0-gpu-jupyter ^
  bash -c "jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --notebook-dir=/tf/code"



https://keras.io/api/applications/