
def get_input(framed):
    #get user input for option: score information, class popularity, skill popularity
    choic=input('1. Attribute Information\n2. Class Popularity\n3. Skill Popularity\n')
    while choic not in ['1','2','3']:
        print('Invalid input. Try again.')
        choic=input('1. Attribute Information\n2. Class Popularity\n3. Skill Popularity\n')
    #if score information
    if choic=='1':
        #show mean,median,max,min among str,spd,mag
        print(f'MP:\nMean: {framed.loc[3].mean()}\nMedian: {framed.loc[3].median()}\nMaximum: {framed.loc[3].max()}\nMinimum: {framed.loc[3].min()}\n')
        print(f'HP:\nMean: {framed.loc[4].mean()}\nMedian: {framed.loc[4].median()}\nMaximum: {framed.loc[4].max()}\nMinimum: {framed.loc[4].min()}\n')
        print(f'Str:\nMean: {framed.loc[5].mean()}\nMedian: {framed.loc[5].median()}\nMaximum: {framed.loc[5].max()}\nMinimum: {framed.loc[5].min()}\n')
        print(f'Atk:\nMean: {framed.loc[6].mean()}\nMedian: {framed.loc[6].median()}\nMaximum: {framed.loc[6].max()}\nMinimum: {framed.loc[6].min()}\n')
        print(f'Def:\nMean: {framed.loc[7].mean()}\nMedian: {framed.loc[7].median()}\nMaximum: {framed.loc[7].max()}\nMinimum: {framed.loc[7].min()}\n')
        print(f'Mag:\nMean: {framed.loc[8].mean()}\nMedian: {framed.loc[8].median()}\nMaximum: {framed.loc[8].max()}\nMinimum: {framed.loc[8].min()}\n')
        print(f'Spr:\nMean: {framed.loc[9].mean()}\nMedian: {framed.loc[9].median()}\nMaximum: {framed.loc[9].max()}\nMinimum: {framed.loc[9].min()}\n')
        print(f'Acc:\nMean: {framed.loc[10].mean()}\nMedian: {framed.loc[10].median()}\nMaximum: {framed.loc[10].max()}\nMinimum: {framed.loc[10].min()}\n')
        print(f'Spd:\nMean: {framed.loc[11].mean()}\nMedian: {framed.loc[11].median()}\nMaximum: {framed.loc[11].max()}\nMinimum: {framed.loc[11].min()}\n')
        print(f'Evs:\nMean: {framed.loc[12].mean()}\nMedian: {framed.loc[12].median()}\nMaximum: {framed.loc[12].max()}\nMinimum: {framed.loc[12].min()}\n')
    #else if class popularity
    elif choic=='2':
        #show classes and percentages from most to leasr self.skills={'archer':{'Snipe':'Ranged weapon range is doubled','Pierce Armor':'Double damage of ranged weapons.'},'knight':{'Parry':'Use a melee attack to negate an enemy\'s next attack','Disarm':'Use a melee attack to remove an enemy\'s weapon.'},'wizard':{'Quick Spell':'Cast two spells as one attack.','Change Spell':'Use melee spell attacks as ranged spell attacks, and ranged spell attacks as melee spell attacks.'}}
        black_mage=framed.loc[1].eq('knight').sum()
        warrior=framed.loc[1].eq('archer').sum()
        theif=framed.loc[1].eq('wizard').sum()
        white_mage=framed.loc[1].eq('wizard').sum()
        print(f'{black_mage/(black_mage+warrior+theif+white_mage)*100}% of characters have the Black mage class.\n{warrior/(black_mage+warrior+theif+white_mage)*100}% of characters have the Warrior class.\n{theif/(black_mage+warrior+theif+white_mage)*100}% of characters have the Theif class.\n{white_mage/(black_mage+warrior+theif+white_mage)*100}% of characters have the White mage class.')