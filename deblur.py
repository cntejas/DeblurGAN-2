import os

combine="python /content/DeblurGAN/datasets/combine_A_and_B.py --fold_A /content/DeblurGAN/datasets/blurred --fold_B /content/DeblurGAN/datasets/clear --fold_AB /content/DeblurGAN/datasets/blur2clear"
os.system(combine)
train = "python /content/DeblurGAN/train.py --dataroot /content/DeblurGAN/datasets/blur2clear --learn_residual --resize_or_crop 'scale_width'"
os.system(train)
test = "python /content/DeblurGAN/test.py --dataroot /content/DeblurGAN/datasets/test --model test --dataset_mode single --results_dir /content/DeblurGAN/datasets/results/ --learn_residual --resize_or_crop 'scale_width'"
# Execute the command
os.system(test)
