""" Функція plants_vs_zombies_nazgaf приймає два аргументи: зомби та растения. Обидва аргументи є списками чисел, які представляють зомбі та рослини відповідно.

Усередині функції ми ініціалізуємо дві змінні survivors_zombies і survivors_plants, які відстежуватимуть кількість вижилих зомбі та рослин відповідно.

Також ми ініціалізуємо дві змінні total_attack_zombies та total_attack_plants, які відстежуватимуть загальну силу атаки зомбі та рослин відповідно.

Потім запускаємо цикл for, який проходить по кожному індексу від 0 до максимальної довжини списків зомби та растения. Це дозволяє нам порівнювати елементи з однаковими індексами, навіть якщо один зі списків коротший за інший.

Усередині циклу ми перевіряємо, чи поточний індекс не виходить за межі довжини будь-якого зі списків. Якщо це так, ми вважаємо це перемогою для тієї сторони, яка не закінчилася.

Якщо індекс у межах обох списків, ми порівнюємо відповідні елементи та збільшуємо відповідний лічильник тих, хто вижив.

Ми також збільшуємо total_attack_zombies та total_attack_plants на значення елемента, якщо він існує у списку.

Після того, як ми пройшли усі елементи, ми перевіряємо умови перемоги. Якщо кількість вижили зомбі більше, ніж рослин, то ми повертаємо False, оскільки зомбі перемогли. Якщо кількість рослин, що вижили, більша, ніж зомбі, то ми повертаємо True, тому що рослини перемогли.

Якщо кількість тих, хто вижив однакову, ми порівнюємо загальну силу атаки зомбі і рослин. Якщо сила атаки зомбі більша, ми повертаємо False, інакше - True. Якщо сили однакові, ми повертаємо True, оскільки це рівнозначно нічиєї.

Наприкінці ми повертаємо True, оскільки це значення за умовчанням, якщо жодна з умов перемоги не виконано. """

def plants_vs_zombies_nazgaf(zombies, plants):
    
    # Кількість рослин та зомбі, що вижили
    
    survivors_zombies = 0
    survivors_plants = 0

    # Сумарна сила атаки З та Р
    
    total_attack_zombies = 0
    total_attack_plants = 0

    # Проходимо масивами і порівнюємо елементи з однаковими індексами
    
    for i in range(max(len( zombies ), len( plants ))):
        
        # Якщо індекс виходить за межі одного з масивів, вважаємо це як перемогу відповідної сторони
        
        if i >= len( zombies ):
            survivors_plants += 1
            
        elif i >= len( plants ):
            survivors_zombies += 1
            
        else:
            
            # Якщо рослина або зомбі мають більше значення, то вона виживає
            
            if zombies[ i ] > plants[ i ]:
                survivors_zombies += 1
                
            elif plants[ i ] > zombies[ i ]:
                survivors_plants += 1

        # Суммуємо силу атаки зомбі та рослин
        total_attack_zombies += zombies[ i ] if i < len( zombies ) else 0
        
        total_attack_plants += plants[ i ] if i < len( plants ) else 0

    # Перевіряємо випадки виграшу та поразок
    
    if survivors_zombies > survivors_plants:
        return False
    
    elif survivors_zombies < survivors_plants:
        return True
    
    elif total_attack_zombies > total_attack_plants:
        return False
    
    elif total_attack_zombies < total_attack_plants:
        return True
    
    else:
        return True

# Тести

print(plants_vs_zombies_nazgaf([1, 3, 5, 7 ], [ 2, 4, 6, 8]))  # True

print(plants_vs_zombies_nazgaf([1, 3, 5, 7], [2, 4]))  # False

print(plants_vs_zombies_nazgaf([1, 3, 5, 7], [2, 4, 0, 8]))  # True

print(plants_vs_zombies_nazgaf([2, 1, 1, 1], [1, 2, 1, 1]))  # True