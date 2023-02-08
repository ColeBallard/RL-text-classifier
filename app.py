IMAGE_CLASSIFICATIONS = {
    0: (0, 1908),
    1: (1930, 4339),
    2: (4367, 5609),
    3: (5635, 7944),
    4: (7976, 14991),
    5: (15018, 15889),
    6: (15920, 18870),
    7: (18888, 20933),
    8: (20961, 21974),
    9: (22005, 28670)
}

def createTrainLabels():
    for num in IMAGE_CLASSIFICATIONS:
        for i in range(IMAGE_CLASSIFICATIONS[num][0], IMAGE_CLASSIFICATIONS[num][1] + 1):
            with open(f'train_labels/rlnum{i}.txt', 'w') as f:
                f.write(f'rlnum{i}.jpg, {num}')

# createTrainLabels()
