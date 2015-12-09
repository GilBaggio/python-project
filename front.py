option = 'yes'

#list of options mapped for each number
while (option == 'yes'):
    print '* * * * * * * * * * * * * * SCENARIOS * * * * * * * * * * * * * * * '
    print '\n1. Number of Boys and Girls in all India level and Total Students'
    print '\n2. Number of Students who got the Maximum score in all India level and the Max score'
    print '\n3. List of states and Count of States'
    print '\n4. Students who scored above 90'
    print '\n5. Statewise Pass percentage'
    print '\n6. Display the Student who got the Highest percentage in a State'
    print '\n7. Pass and Fail percentage in each State and Rural/Urban'
    print '\n8. Head counts in each Difficulty level'
    print '\n9. Highest percentage in all india level'
    print '\n10. Highest scorers in each difficulty level'
    print '\n11. List of all mediums and count and number of Boys/Girls'    
    print '__________________________________________________________________________'    
    value = input("Enter the Scenario number:")
    print '\n'
    
    # condition statements for checking the option
    if value == 1:
        import scen1
        scen1.gender_count()
    elif value == 2:
        import scen2
        scen2.max_score()
    elif value == 3:
        import scen3
        scen3.state_count()
    elif value == 4:
        import scen4
        scen4.higher_level()
    elif value == 5:
        print '\n-Individual States'
        print '\n1.Andaman & Nicobar Islands(AN)'
        print '\n2.Andhra Pradesh(AP)'
        print '\n3.Arunachal Pradesh(AR)'
        print '\n4.Bihar(BR)'
        print '\n5.Chhattisgarh(CG)'
        print '\n6.Chandigarh(CH)'
        print '\n7.Daman & Diu(DD)'
        print '\n8.Delhi(DL)'
        print '\n9.Dadra & Nagar Haveli(DN)'
        print '\n10.Goa(GA)'
        print '\n11.Gujarat(GJ)'
        print '\n12.Himachal Pradesh(HP)'
        print '\n13.Haryana(HR)'
        print '\n14.Jharkhand(JH)'
        print '\n15.Jammu & Kashmir(JK)'
        print '\n16.Karnataka(KA)'
        print '\n17.Kerala(KL)'
        print '\n18.Meghalaya(MG)'
        print '\n19.Maharashtra(MH)'
        print '\n20.Manipur(MN)'
        print '\n21.Madhya Pradesh(MP)'
        print '\n22.Mizoram(MZ)'
        print '\n23.Nagaland(NG)'
        print '\n24.Orissa(OR)'
        print '\n25.Punjab(PB)'
        print '\n26.Puducherry(PY)'
        print '\n27.Rajasthan(RJ)'
        print '\n28.Sikkim(SK)'
        print '\n29.Tamil Nadu(TN)'
        print '\n30.Tripura(TR)'
        print '\n31.Uttarakhand(UK)'
        print '\n32.Uttar Pradesh(UP)'
        print '\n33.West Bengal(WB)'
              
        import scen5
        scen5.state_pass()
    elif value == 6:
        print '\n-Individual States'
        print '\n1.Andaman & Nicobar Islands(AN)'
        print '\n2.Andhra Pradesh(AP)'
        print '\n3.Arunachal Pradesh(AR)'
        print '\n4.Bihar(BR)'
        print '\n5.Chhattisgarh(CG)'
        print '\n6.Chandigarh(CH)'
        print '\n7.Daman & Diu(DD)'
        print '\n8.Delhi(DL)'
        print '\n9.Dadra & Nagar Haveli(DN)'
        print '\n10.Goa(GA)'
        print '\n11.Gujarat(GJ)'
        print '\n12.Himachal Pradesh(HP)'
        print '\n13.Haryana(HR)'
        print '\n14.Jharkhand(JH)'
        print '\n15.Jammu & Kashmir(JK)'
        print '\n16.Karnataka(KA)'
        print '\n17.Kerala(KL)'
        print '\n18.Meghalaya(MG)'
        print '\n19.Maharashtra(MH)'
        print '\n20.Manipur(MN)'
        print '\n21.Madhya Pradesh(MP)'
        print '\n22.Mizoram(MZ)'
        print '\n23.Nagaland(NG)'
        print '\n24.Orissa(OR)'
        print '\n25.Punjab(PB)'
        print '\n26.Puducherry(PY)'
        print '\n27.Rajasthan(RJ)'
        print '\n28.Sikkim(SK)'
        print '\n29.Tamil Nadu(TN)'
        print '\n30.Tripura(TR)'
        print '\n31.Uttarakhand(UK)'
        print '\n32.Uttar Pradesh(UP)'
        print '\n33.West Bengal(WB)'
        
        import scen6
        scen6.state_high()
    elif value == 7:
        print '\n-Individual States'
        print '\n1.Andaman & Nicobar Islands(AN)'
        print '\n2.Andhra Pradesh(AP)'
        print '\n3.Arunachal Pradesh(AR)'
        print '\n4.Bihar(BR)'
        print '\n5.Chhattisgarh(CG)'
        print '\n6.Chandigarh(CH)'
        print '\n7.Daman & Diu(DD)'
        print '\n8.Delhi(DL)'
        print '\n9.Dadra & Nagar Haveli(DN)'
        print '\n10.Goa(GA)'
        print '\n11.Gujarat(GJ)'
        print '\n12.Himachal Pradesh(HP)'
        print '\n13.Haryana(HR)'
        print '\n14.Jharkhand(JH)'
        print '\n15.Jammu & Kashmir(JK)'
        print '\n16.Karnataka(KA)'
        print '\n17.Kerala(KL)'
        print '\n18.Meghalaya(MG)'
        print '\n19.Maharashtra(MH)'
        print '\n20.Manipur(MN)'
        print '\n21.Madhya Pradesh(MP)'
        print '\n22.Mizoram(MZ)'
        print '\n23.Nagaland(NG)'
        print '\n24.Orissa(OR)'
        print '\n25.Punjab(PB)'
        print '\n26.Puducherry(PY)'
        print '\n27.Rajasthan(RJ)'
        print '\n28.Sikkim(SK)'
        print '\n29.Tamil Nadu(TN)'
        print '\n30.Tripura(TR)'
        print '\n31.Uttarakhand(UK)'
        print '\n32.Uttar Pradesh(UP)'
        print '\n33.West Bengal(WB)'
        import scen7
        scen7.pass_fail()
    elif value == 8:
        import scen8
        scen8.head_count()
    elif value == 9:
        import scen9
        scen9.high_percentage()
    elif value == 10:
        import scen10
        scen10.high_difficulty_level() 
    elif value == 11:
        import scen11
        scen11.med_list()     
    else:
        print"Enter number between 1-11"
        
     #statements for the user to choose whether he wants to continue or not
    print "\nyes.Continue \n no.Exit"
    for i in range(10):
        option = raw_input("Select yes or no:")
        if(option != "yes" and option != "no"):
            print "\n"
            print "Invalid entry-Please enter \"yes\" or \"no\""
            continue;
        else:
            break;
  
