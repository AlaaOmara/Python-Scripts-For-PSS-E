# PSSE Python Scripts

A collection of Python scripts for Power System Simulation Environment (PSSE) automation and analysis.

## Scripts

### Switched Shunt Capacitor Adjustment (`Sw_Shnt_Cap_Adjust.py`)

This script performs automatic reactive power compensation using installed switched shunt capacitors in a power system.

#### Description

The script adjusts switched shunt capacitor settings based on the reactive power demand at each bus in a selected subsystem. It optimizes capacitor block allocation to achieve near-zero power factor at each bus.

#### How It Works

1. **Subsystem Selection**: Selects a specific bus system for compensation
2. **Reactive Power Analysis**: Reads the total reactive power (MVAr) at each bus
3. **Capacitor Optimization**: Calculates the optimal number of capacitor blocks needed based on:
   - Total available MVAr capacity
   - Individual block size
   - Control criterion (default: remainder ≥ 5 MVAr)
4. **Power Flow Analysis**: Runs load flow calculations to verify the compensation

#### Installation & Usage

##### Requirements
- Python 3
- PSSE with psspy module installed

##### Steps

1. **Place the script** in the same folder as your PSSE case file
2. **Customize the subsystem**:
   - Modify the first line of the script to select your desired subsystem:
     ```python
     psspy.bsys(1,1,[start_bus, end_bus],0,[],0,[],0,[],28,[1,])
     ```
   - **Tip**: Record the subsystem selection as Python code directly in PSSE GUI, then copy the generated line into this script
3. **Run the script** from within PSSE Python environment

#### Customization

You can modify the control criteria for capacitor block switching:

- **Current criterion**: Capacitor blocks are added if the remainder (modulo) of load MVAr divided by block size is ≥ 5
- To change this threshold, modify this line:
  ```python
  elif MVAr_value % size_block >= 5 :  # Change the number 5 to your desired threshold
  ```

#### Parameters Explained

- `nBlock`: Number of available capacitor blocks at each bus
- `size_block`: MVAr capacity of each individual block
- `max_MVAr`: Maximum total reactive power compensation available (nBlock × size_block)
- `MVAr_value`: Current reactive power demand at the bus
- `sw_shnt_cap`: Final calculated capacitor setting to be applied

#### Output

The script prints the maximum available MVAr at each bus and performs load flow analysis to validate the compensation.

#### Control Logic

The script uses the following decision tree for each bus:

```
IF reactive power >= max available capacity
    → Set to maximum capacity
ELSE IF block size is 0
    → Set to 0
ELSE IF (reactive power % block size) >= 5
    → Round UP to nearest block
ELSE
    → Round DOWN to nearest block
```

#### License

MIT License - See LICENSE file for details

#### Author

Created for power system reactive power compensation automation
