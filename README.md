# Dota 2 Grid Editor

# Installation


## Using Manually
1. Download as zip
2. Unzip
3. Edit _USER_DATA.py
4. Use execute.py to make grids, use data_collector.py to refresh hero stats

```python

    role_grid('name_of_grid',list_of_heroes)
    create_hero_grid('name_of_grid', column_to_sort_by)
    
```

Execute.py editing documentation.

    Main Class For Making Grids

    ...

    Methods
    -------
    create_hero_grid(grid_name,column_to_sort_by,which_hero_list,heroes_per_line)
        Parameters
        ----------
        grid_name : str
            Name of the grid.
        sort_by : str
            column to sort by, for example ('winrate','personal_match_played').
        heroes_list : str
            'all' for of all heroes, 'played' for using heroes you've at least played for 2 matches.
        
        
        
    role_grid(grid_name,column_to_sort_by,which_hero_list)
        Parameters
        ----------
        grid_name : str
            Name of the grid.
        sort_by : str
            column to sort by, for example ('winrate','personal_match_played').
        heroes_list : str
            'all' for of all heroes, 'played' for using heroes you've at least played for 2 matches.