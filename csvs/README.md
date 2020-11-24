# Description of each CSV dataset

#### birthdays-since-1985.csv
Two columns: ``Player_ID`` and ``Birthday``. This is a map of the birthday of each NBA lottery pick prospect since 1985.
The ``Player_ID`` column corresponds with ``PERSON_ID`` of the ``draft_data_api.csv`` file.

#### draftYears.csv
Simple file, two columns: ``Season``, ``Draft_Date``. For each NBA season, this file contains the exact date of the draft.

#### draft_data_api.csv
The real "workhorse" file, containing the names, ids, team that drafted the player, etc. of all lottery picks from 1985 - 2020.
The set of attributes for each row are: (``PERSON_ID``, ``PLAYER_NAME``, ``SEASON``, ``ROUND_NUMBER``, ``ROUND_PICK``, ``OVERALL_PICK``,
``DRAFT_TYPE``, ``TEAM_ID``, ``TEAM_CITY``, ``TEAM_NAME``, ``TEAM_ABBREVIATION``, ``ORGANIZATION``, 
``ORGANIZATION_TYPE``, ``PLAYER_PROFILE_FLAG``).
