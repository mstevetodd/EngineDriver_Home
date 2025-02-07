*******************************************
Changes / Updates
*******************************************

.. meta::
   :keywords: versions changes

.. include:: ../include.rst

Production Changes
--------------------------------------------

Changes included in Engine Driver production version **2.37.187**:

* Support for 32 Function Roster Entries
* New WiThrottle "CV Programming on Main" page. (note: not supported on all Command Stations)
* New preference to allow for double back button presses to exit the app
* Option to have the Throttle WebView on the top of the page
* Discovery of JMRI DCCppOverTCP Server.
* Include any server with port 2560 as a DCC-EX server when connection preference set to 'Auto'
* Change the owner filter pref default to false
* UI improvements for the DCC-EX and Function Defaults pages
* Added intro/setup wizard page for DCC-EX
* Action Bar UI improvements
* Change all toolbar/Action Bar icons to vectors for better scaling and reduce maintenance effort
* Reworking of the 'Original' theme. Buttons changed to vectors
* Removal of duplicate icons
* Bug fixes for the 'keyboard' gamepad type
* Bug fix for the close button in function_defaults
* Bug fix for Consist Light Editing
* Bug fix for DCC-EX default latching for non-roster locos
* Bug fix for initial Auto-Web preference change
* Bug fix for fastclock
* lint removal
* New Button to sort Turnouts/Points by Name or ID
* New Button to sort Routes by Name or ID
* Additional French Translations by Alain Carasso
* New button to download the roster list to the Recents list
* Selecting a loco from Recent Locos will attempt to restore the function button labels
* Move targetSDK from 33 to 34 per Google requirement by 2024-8-30
* Automatically reduce the font size of buttons if the first word is long or the total text length is long
* Preference to always show the Throw and Close buttons for Turnouts/Points
* Additional Google Translations

Beta Changes
--------------------------------------------

Changes included in Engine Driver Beta version **2.38.193**:

* Preference to always show the Throw and Close buttons for Turnouts/Points
* New 'Neon Blue' theme
* Japanese translations by Futoshi Yanagi
* French Canadian translations by Yvéric Patry
* Support DCC-EX remote drop of a loco (FORGET)
* On Horizontal slider layouts, preference to auto show/hide the function buttons of the non-active (volume) throtttle
* Fix for the change to the DCC-EX response/broadcast for AUTO Track Manager outputs
* Fix for the DCC-EX AUTO track type change command
* Bug fixes for the Consist Follow Functions feature
* Send heartbeat restart on reconnect
* Bug fix for 'No' option for the DCC-EX protocol option
* New Semi-Realistic Throttle screen layout
* Added ability to override the WiThrottle default Latching
* Support for new gamepad type - Auvisio Android-B
* Reinstate missing label on the Select Button
* Improvement to the roster sorting options
* Linting and code cleanup
* Added shake action option for Emergency Stop
* Additional Google Translations
* Significant changes to the Semi-Realistic Throttle, and in particular, the integration with decoders, with assistance from John Geddes
* Significant re-write of the air brake system in the Semi-Realistic Throttle
* Bug fix for DCC-EX roster entries with no functions. Was previously not possible to have no functions show for a roster entry 
* New Preference to override the bug fix for roster entries with no functions
* Additional French Translations by Alain Carasso


Complete ChangeLog
--------------------------------------------

`view complete changelog <https://raw.githubusercontent.com/JMRI/EngineDriver/master/changelog-and-todo-list.txt>`_

