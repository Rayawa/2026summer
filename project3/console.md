//train.py
```
50 epochs completed in 3.074 hours.
Optimizer stripped from D:\python\2026summer\project3\runs\detect\train\weights\last.pt, 5.5MB
Optimizer stripped from D:\python\2026summer\project3\runs\detect\train\weights\best.pt, 5.5MB

Validating D:\python\2026summer\project3\runs\detect\train\weights\best.pt...
Ultralytics 8.4.48  Python-3.12.13 torch-2.7.1+cu118 CUDA:0 (NVIDIA GeForce RTX 5060 Laptop GPU, 8151MiB)
YOLO11n summary (fused): 101 layers, 2,582,737 parameters, 0 gradients, 6.3 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 19/19 6.8it/s 2.8s
                   all        588        406      0.943      0.891       0.94      0.697
                 Paper        134        141      0.936      0.894      0.936       0.69
                  Rock        125        147      0.949      0.898      0.943      0.689
              Scissors        114        118      0.944      0.881       0.94      0.714
Speed: 0.2ms preprocess, 2.1ms inference, 0.0ms loss, 0.8ms postprocess per image
Results saved to D:\python\2026summer\project3\runs\detect\train
```

//evaluate.py
```
Ultralytics 8.4.48  Python-3.12.13 torch-2.7.1+cu118 CUDA:0 (NVIDIA GeForce RTX 5060 Laptop GPU, 8151MiB)
YOLO11n summary (fused): 101 layers, 2,582,737 parameters, 0 gradients, 6.3 GFLOPs
val: Fast image access  (ping: 0.10.0 ms, read: 194.9107.2 MB/s, size: 30.5 KB)
val: Scanning D:\python\2026summer\project3\rock-paper-scissors-11\valid\labels.cache... 588 images, 247 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 588/588  0.0s
WARNING NMS time limit 2.050s exceeded
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 37/37 1.9it/s 20.0s
                   all        588        406      0.942      0.891       0.94      0.697
                 Paper        134        141      0.934      0.894      0.936       0.69
                  Rock        125        147      0.949      0.898      0.943      0.689
              Scissors        114        118      0.944      0.881       0.94      0.713
Speed: 1.3ms preprocess, 5.3ms inference, 0.0ms loss, 0.5ms postprocess per image
Results saved to D:\python\2026summer\project3\runs\detect\val
mAP50-95: 0.697
mAP50: 0.940
```

//test.py
```
Ultralytics 8.4.48  Python-3.12.13 torch-2.7.1+cu118 CUDA:0 (NVIDIA GeForce RTX 5060 Laptop GPU, 8151MiB)
YOLO11n summary (fused): 101 layers, 2,582,737 parameters, 0 gradients, 6.3 GFLOPs
val: Fast image access  (ping: 0.30.1 ms, read: 51.312.0 MB/s, size: 27.9 KB)
val: Scanning D:\python\2026summer\project3\rock-paper-scissors-11\test\labels... 245 images, 98 backgrounds, 0 corrupt: 77% ━━━━━━━━━─── 245/320val: Scanning D:\python\2026summer\project3\rock-paper-scissors-11\test\labels... 320 images, 132 backgrounds, 0 corrupt: 100% ━━━━━━━━━━━━ 320/320 2.6Kit/s 0.1s
val: New cache created: D:\python\2026summer\project3\rock-paper-scissors-11\test\labels.cache
WARNING NMS time limit 2.050s exceeded
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100% ━━━━━━━━━━━━ 20/20 1.3it/s 15.2s
                   all        320        210      0.898       0.92      0.934      0.693
                 Paper         72         72      0.868      0.861      0.904       0.63
                  Rock         63         72      0.938      0.944      0.951      0.715
              Scissors         64         66      0.887      0.953      0.947      0.734
Speed: 1.9ms preprocess, 2.8ms inference, 0.0ms loss, 0.6ms postprocess per image
Results saved to D:\python\2026summer\project3\runs\detect\val-2
mAP50-95: 0.693
mAP50: 0.934
```