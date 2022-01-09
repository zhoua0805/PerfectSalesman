# PerfectSalesman
ML predictor on the best product to go on sale for a specified month

**Presentation link: https://docs.google.com/presentation/d/13gSs0TwK4Tyng-geULDqnelH4AA37jt4hWeHAq5YNIU/edit#slide=id.g10ccc3e8753_0_586**

## Set up
* clone this repo: `git clone https://github.com/zhoua0805/PerfectSalesman`
* download dependencies: `python requirements.txt`

## Demo
Run `/python/interface/demo.py`:
```terminal
Welcome to PerfectSalesman!
Do you want to find the best product to go on sale for this month (a),
or input a custom data point (b),
or exit (q)?
________________
```

### Option 1: Get the best product to go on sale
```
a
----------------------------------------------------------------------
The best product to go in sale in january is: Copiers for 95%.
You will gain $9197.07 in profit with 652 Qty sold.
----------------------------------------------------------------------
```
### Option 2: Input a product, custom discount value, and get predicted sales, profit, and quantity
```
b
Please enter a product category: Art
Please enter discount percentage (format: dd%): 50
----------------------------------------------------------------------
You will gain $4797.88 in profit with 340 Qty sold.
----------------------------------------------------------------------
```
![image](https://user-images.githubusercontent.com/46226072/148684825-bb373595-b8a0-4efb-acf9-c9e0d0b78df3.png)
![image](https://user-images.githubusercontent.com/46226072/148684848-6b1f5c8c-c413-40a6-be8a-e62822a94604.png)

## Training
Go to `/python` folder and run 
```python
main.py epochs=100 batchsize=16 lr=0.001
```
and replace the arguments with hyperparameters of your choice
