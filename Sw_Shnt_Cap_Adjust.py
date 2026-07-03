import math

#selected subsystem (SWitched shunt capacitor adjust)
psspy.bsys(1,1,[ 0, 50],0,[],0,[],0,[],28,[1,]) # select you own bus system as required, you can do that by recording python in PSSE case

b_number = psspy.abusint(1, 1, 'NUMBER')[1][0]
for bus_number in b_number:
    MVAr_value = psspy.busdt2(bus_number, 'TOTAL', 'NOM')[1].imag
    if psspy.swsint(bus_number, 'BLOCKS')[0] == 0 :
        nBlock = psspy.swsint(bus_number, 'BLOCKS')[1]  #get the number of blocks at specified load bus
        size_block = psspy.swsblk(bus_number, 1)[2]  #get the block MVAr size of each block
        max_MVAr = nBlock*size_block
        print(max_MVAr)
        if MVAr_value >= max_MVAr : sw_shnt_cap = max_MVAr
        elif size_block == 0 : 
            sw_shnt_cap = 0
        elif MVAr_value % size_block >= 5 : # modulos(remainder) of  load MVAr and capacitor used blocks, you can change the number as per your control criteria (here it will operate if modulos equal or gretear than five)
            sw_shnt_cap= math.ceil(MVAr_value/size_block)*size_block 
        elif  MVAr_value % size_block <5 :
             sw_shnt_cap= math.floor(MVAr_value/size_block)*size_block 
        psspy.switched_shunt_chng_3(bus_number,[_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i,_i],[_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,sw_shnt_cap,_f],_s)

psspy.fdns([0,0,0,0,0,1,-1,0])
psspy.fdns([1,0,0,0,0,1,0,0])
psspy.fdns([0,0,0,0,0,1,99,0])
