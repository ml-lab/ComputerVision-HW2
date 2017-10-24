EN.601.661 – Computer Vision - Homework 2
-----------------------------------------
### To View This
This is a readme written in markdown. You can access [here](https://github.com/joe-siyuan-qiao/ComputerVision-HW2) to view it online.

### How to Run
```bash
# The results will be found in ./results/
python hw2.py
```
We also provide the pre-computed outputs in the directory _./results_

### Development Environment
| Package       | Version       |
| ------------- |:-------------:|
| Python        | 2.7.10        |
| NumPy         | 1.13.3        |
| OpenCV        | 3.3.0         |
| matplotlib    | 1.5.3         |
| SymPy         | 1.1.1         |

### The Corner Detection Results
The corner detection result of bikes1  
![corner detection of bikes1](results/bikes1_corners.png)

The corner detection result of bikes2  
![corner detection of bikes2](results/bikes2_corners.png)

The corner detection result of bikes3  
![corner detection of bikes3](results/bikes3_corners.png)

The corner detection result of graf1  
![corner detection of graf1](results/graf1_corners.png)

The corner detection result of graf2  
![corner detection of graf2](results/graf2_corners.png)

The corner detection result of graf3  
![corner detection of graf3](results/graf3_corners.png)

The corner detection result of leuven1  
![corner detection of leuven1](results/leuven1_corners.png)

The corner detection result of leuven2  
![corner detection of leuven2](results/leuven2_corners.png)

The corner detection result of leuven3  
![corner detection of leuven3](results/leuven3_corners.png)

The corner detection result of wall1  
![corner detection of wall1](results/wall1_corners.png)

The corner detection result of wall2  
![corner detection of wall2](results/wall2_corners.png)

The corner detection result of wall3  
![corner detection of wall3](results/wall3_corners.png)

### The Matching Results using the Sum-of-Squared-Distance
bikes1 and bikes2  
![ssd matching bikes1 and bikes2](results/bikes1_bikes2_matches.png)
The matchings between the two images look very good.

bikes1 and bikes3  
![ssd matching bikes1 and bikes3](results/bikes1_bikes3_matches.png)
The matchings between the two images look very good.

graf1 and graf2  
![ssd matching graf1 and graf2](results/graf1_graf2_matches.png)
The matchings between the two images look very good.

graf1 and graf3  
![ssd matching graf1 and graf3](results/graf1_graf3_matches.png)
The matchings between the two images are not very ideal.
This is probably due to the big rotation which change the appearance.

leuven1 and leuven2  
![ssd matching leuven1 and leuven2](results/leuven1_leuven2_matches.png)
The matchings between the two images are not very ideal.
This is probably due to the big lighting difference between the two images.

leuven1 and leuven3  
![ssd matching leuven1 and leuven3](results/leuven1_leuven3_matches.png)
The matchings between the two images are not very ideal.
This is probably due to the big lighting difference between the two images.

wall1 and wall2  
![ssd matching wall1 and wall2](results/wall1_wall2_matches.png)
The matchings between the two images are not very ideal.
This is probably due to the fact that the walls have repeating patterns and everywhere looks similar.

wall1 and wall3  
![ssd matching wall1 and wall3](results/wall1_wall3_matches.png)
The matchings between the two images are not very ideal.
This is probably due to the fact that the walls have repeating patterns and everywhere looks similar.

### The Matching Results using the Simple-SIFT
bikes1 and bikes2  
![ssift matching bikes1 and bikes2](results/bikes1_bikes2_ssift_matches.png)
The matchings between the two images look very good.

bikes1 and bikes3  
![ssift matching bikes1 and bikes3](results/bikes1_bikes3_ssift_matches.png)
The matchings between the two images look very good.

graf1 and graf2  
![ssift matching graf1 and graf2](results/graf1_graf2_ssift_matches.png)
The matchings between the two images look very good.

graf1 and graf3  
![ssift matching graf1 and graf3](results/graf1_graf3_ssift_matches.png)
The matchings between the two images are not very ideal.
This is probably due to the big rotation which change the appearance.

leuven1 and leuven2  
![ssift matching leuven1 and leuven2](results/leuven1_leuven2_ssift_matches.png)
The matchings between the two images look very good.

leuven1 and leuven3  
![ssift matching leuven1 and leuven3](results/leuven1_leuven3_ssift_matches.png)
The matchings between the two images look very good.

wall1 and wall2  
![ssift matching wall1 and wall2](results/wall1_wall2_ssift_matches.png)
The matchings between the two images are sparse but accurate.

wall1 and wall3  
![ssift matching wall1 and wall3](results/wall1_wall3_ssift_matches.png)
The matchings between the two images are not very ideal.
This is probably due to the big rotation that changes the distributions of the gradients.

### RANSAC and Stitching using Affine and SSD
bikes1 and bikes2  
![ransac bikes1 and bikes2](results/bikes2_affine_ransac_with_bikes1.png)
![stitch bikes1 and bikes2](results/bikes2_affine_stitch_with_bikes1.png)

bikes1 and bikes3  
![ransac bikes1 and bikes3](results/bikes3_affine_ransac_with_bikes1.png)
![stitch bikes1 and bikes3](results/bikes3_affine_stitch_with_bikes1.png)

graf1 and graf2  
![ransac graf1 and graf2](results/graf2_affine_ransac_with_graf1.png)
![stitch graf1 and graf2](results/graf2_affine_stitch_with_graf1.png)

graf1 and graf3  
![ransac graf1 and graf3](results/graf3_affine_ransac_with_graf1.png)
![stitch graf1 and graf3](results/graf3_affine_stitch_with_graf1.png)

leuven1 and leuven2  
![ransac leuven1 and leuven2](results/leuven2_affine_ransac_with_leuven1.png)
![stitch leuven1 and leuven2](results/leuven2_affine_stitch_with_leuven1.png)

leuven1 and leuven3  
![ransac leuven1 and leuven3](results/leuven3_affine_ransac_with_leuven1.png)
![stitch leuven1 and leuven3](results/leuven3_affine_stitch_with_leuven1.png)

wall1 and wall2  
![ransac wall1 and wall2](results/wall2_affine_ransac_with_wall1.png)
![stitch wall1 and wall2](results/wall2_affine_stitch_with_wall1.png)

wall1 and wall3  
![ransac wall1 and wall3](results/wall3_affine_ransac_with_wall1.png)
![stitch wall1 and wall3](results/wall3_affine_stitch_with_wall1.png)

### RANSAC and Stitching using Perspective and SSD
bikes1 and bikes2  
![ransac bikes1 and bikes2](results/bikes2_perspective_ransac_with_bikes1.png)
![stitch bikes1 and bikes2](results/bikes2_perspective_stitch_with_bikes1.png)

bikes1 and bikes3  
![ransac bikes1 and bikes3](results/bikes3_perspective_ransac_with_bikes1.png)
![stitch bikes1 and bikes3](results/bikes3_perspective_stitch_with_bikes1.png)

graf1 and graf2  
![ransac graf1 and graf2](results/graf2_perspective_ransac_with_graf1.png)
![stitch graf1 and graf2](results/graf2_perspective_stitch_with_graf1.png)

graf1 and graf3  
![ransac graf1 and graf3](results/graf3_perspective_ransac_with_graf1.png)
![stitch graf1 and graf3](results/graf3_perspective_stitch_with_graf1.png)

leuven1 and leuven2  
![ransac leuven1 and leuven2](results/leuven2_perspective_ransac_with_leuven1.png)
![stitch leuven1 and leuven2](results/leuven2_perspective_stitch_with_leuven1.png)

leuven1 and leuven3  
![ransac leuven1 and leuven3](results/leuven3_perspective_ransac_with_leuven1.png)
![stitch leuven1 and leuven3](results/leuven3_perspective_stitch_with_leuven1.png)

wall1 and wall2  
![ransac wall1 and wall2](results/wall2_perspective_ransac_with_wall1.png)
![stitch wall1 and wall2](results/wall2_perspective_stitch_with_wall1.png)

wall1 and wall3  
![ransac wall1 and wall3](results/wall3_perspective_ransac_with_wall1.png)
![stitch wall1 and wall3](results/wall3_perspective_stitch_with_wall1.png)

### RANSAC and Stitching using Affine and SSIFT
bikes1 and bikes2  
![ransac bikes1 and bikes2](results/bikes2_ssift_affine_ransac_with_bikes1.png)
![stitch bikes1 and bikes2](results/bikes2_ssift_affine_stitch_with_bikes1.png)
Using SSIFT produces similar but a little bit worse result.
This is probably due to that the second image is blurred thus has less clear gradients.

bikes1 and bikes3  
![ransac bikes1 and bikes3](results/bikes3_ssift_affine_ransac_with_bikes1.png)
![stitch bikes1 and bikes3](results/bikes3_ssift_affine_stitch_with_bikes1.png)
Using SSIFT produces similar but a little bit worse result.
This is probably due to that the third image is blurred thus has less clear gradients.

graf1 and graf2  
![ransac graf1 and graf2](results/graf2_ssift_affine_ransac_with_graf1.png)
![stitch graf1 and graf2](results/graf2_ssift_affine_stitch_with_graf1.png)
Using SSIFT produces similar result.

graf1 and graf3  
![ransac graf1 and graf3](results/graf3_ssift_affine_ransac_with_graf1.png)
![stitch graf1 and graf3](results/graf3_ssift_affine_stitch_with_graf1.png)
Using SSIFT cannot produce good result, either.

leuven1 and leuven2  
![ransac leuven1 and leuven2](results/leuven2_ssift_affine_ransac_with_leuven1.png)
![stitch leuven1 and leuven2](results/leuven2_ssift_affine_stitch_with_leuven1.png)
Using SSIFT produces result that is much better than using SSD.
This is because the lighting changes do not change the distribution of gradients too much.

leuven1 and leuven3  
![ransac leuven1 and leuven3](results/leuven3_ssift_affine_ransac_with_leuven1.png)
![stitch leuven1 and leuven3](results/leuven3_ssift_affine_stitch_with_leuven1.png)
Using SSIFT produces result that is much better than using SSD.
This is because the lighting changes do not change the distribution of gradients too much.

wall1 and wall2  
![ransac wall1 and wall2](results/wall2_ssift_affine_ransac_with_wall1.png)
![stitch wall1 and wall2](results/wall2_ssift_affine_stitch_with_wall1.png)
Using SSIFT produces result that is much better than using SSD.
But I think this is due to the mechanism we use to determine the matchings between two points.

wall1 and wall3  
![ransac wall1 and wall3](results/wall3_ssift_affine_ransac_with_wall1.png)
![stitch wall1 and wall3](results/wall3_ssift_affine_stitch_with_wall1.png)
Using SSIFT cannot produce good result, either.

### RANSAC and Stitching using Perspective and SSIFT
bikes1 and bikes2  
![ransac bikes1 and bikes2](results/bikes2_ssift_perspective_ransac_with_bikes1.png)
![stitch bikes1 and bikes2](results/bikes2_ssift_perspective_stitch_with_bikes1.png)

bikes1 and bikes3  
![ransac bikes1 and bikes3](results/bikes3_ssift_perspective_ransac_with_bikes1.png)
![stitch bikes1 and bikes3](results/bikes3_ssift_perspective_stitch_with_bikes1.png)

graf1 and graf2  
![ransac graf1 and graf2](results/graf2_ssift_perspective_ransac_with_graf1.png)
![stitch graf1 and graf2](results/graf2_ssift_perspective_stitch_with_graf1.png)

graf1 and graf3  
![ransac graf1 and graf3](results/graf3_ssift_perspective_ransac_with_graf1.png)
![stitch graf1 and graf3](results/graf3_ssift_perspective_stitch_with_graf1.png)

leuven1 and leuven2  
![ransac leuven1 and leuven2](results/leuven2_ssift_perspective_ransac_with_leuven1.png)
![stitch leuven1 and leuven2](results/leuven2_ssift_perspective_stitch_with_leuven1.png)

leuven1 and leuven3  
![ransac leuven1 and leuven3](results/leuven3_ssift_perspective_ransac_with_leuven1.png)
![stitch leuven1 and leuven3](results/leuven3_ssift_perspective_stitch_with_leuven1.png)

wall1 and wall2  
![ransac wall1 and wall2](results/wall2_ssift_perspective_ransac_with_wall1.png)
![stitch wall1 and wall2](results/wall2_ssift_perspective_stitch_with_wall1.png)

wall1 and wall3  
![ransac wall1 and wall3](results/wall3_ssift_perspective_ransac_with_wall1.png)
![stitch wall1 and wall3](results/wall3_ssift_perspective_stitch_with_wall1.png)

