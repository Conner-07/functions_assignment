def dice_stats():
    # Get dice configuration and target sum from user input
    dice_type = input("Please enter the dice configuration or just the number of sides for one die): ")
    total_sum = int(input("Please enter the target sum: "))
    
    # Extract the dice configurations using the d in the user input for the test cases
    num_dice, num_sides = [int(value) for value in dice_type.split("d")]
    

    total_outcomes = num_sides ** num_dice
    
    # Initialize count of favorable outcomes
    favorable_outcomes = 0
    
    # Calculate the number of outcomes reach or go over the target
    for roll in range(1, num_sides + 1):
        if num_dice == 1:
            if roll >= total_sum:
                favorable_outcomes += 1
        else:
            sub_total_sum = total_sum - roll
            if sub_total_sum > 0:
                favorable_outcomes += min(sub_total_sum, num_sides) ** (num_dice - 1)
    
    # Calculate and return probability
    total_prob = favorable_outcomes / total_outcomes
    return total_prob


probability = dice_stats()
print("The probability of achieving the target sum is" (probability))

def permutations(input_string):
    if len(input_string) <= 1:
        return [input_string]

    perms = []

    # Iterate through each character 
    for i in range(len(input_string)):

        prefix = input_string[i]
        
        suffix = input_string[:i] + input_string[i+1:]

        for perm in permutations(suffix):
     
            perms.append(prefix + perm)

   
    return perms