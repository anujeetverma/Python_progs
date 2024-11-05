

def count_substring(string, sub_string):
    subset_len = len(sub_string)
    subsets = [string[i:i+subset_len]for i in range(len(string)- subset_len+1)]
    count =0
    for subset in subsets:
        if subset == sub_string:
            count = count+1
        
            
    return count


# Sample Input

# ABCDCDC
# CDC
# Sample Output
# 2
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)