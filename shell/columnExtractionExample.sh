cat test.dat | cut -d " " -f 1,3
# Notes:
# The cut command does not regard the multiple spaces as an single delimeter. 
# Ex: (_ is space)
#   a_b_c -> a b c
#   a___b_c -> a _ b c
