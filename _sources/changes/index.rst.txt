*******************************************
Changes / Updates
*******************************************

.. meta::
   :keywords: versions changes

.. include:: ../include.rst

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
      :local:
      :depth: 3

Production Changes
--------------------------------------------

Changes included in Engine Driver Production version **2.39.195**:

* When you change throttle layouts, and the new layout supports a range of throttles, Engine Driver will ask for the number.
* Send additional resync requests after DCC-EX reconnect
* Added option to sequence the loading of items on DCC-EX
* Bug fix for F0-F9 on some systems - Removed leading zero from FKey id when sending
* Bug fix for Immersive mode
* Cleanup of the Horizontal Throttle layouts. Fixing some height issues

Changes included in Engine Driver Production version **2.38.193**:

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

Beta Changes
--------------------------------------------

Changes included in Engine Driver Beta version **2.40.201**:

* Bug fixes for the Semi-Realistic Throttle
* added a new separate check for when the app is in background
* reduce the amount of static text related to log messages
* wholesale cleanup if the code to 'finish' an activity
* Additional log messages in select_loco
* Move to AndroidX libraries
* Added support for ESU MC Pro. Additional + removed + default options for the MC Pro
* Bug fix for PoM programming of DCC addresses 1 and 2
* Preference to using large toolbar buttons. Defaults to large on screens larger than 6.7"/17cm.
* Preference screen numeric input dialogs show the keypad not the full keyboard
* ESU MC2/Pro fixes to support the SRT
* Gradle upgrade
* targetSDK raised to 35 - Had to go back to TargetSdk 35 from 36 to get around the edge-to-edge enforcement on Android 16
* Children's timer changes. Passwords changed to PINs (numeric). Some bug fixes. Added Kiosk mode option. Added Demo mode option.
* Bug fix for the brake slider on the ESU MC Pro
* Bug fix for when changing to a throttle screen layout with more possible throttles
* Added Option for single throttle EStop on long press of 'stop' button
* Fix NPE when changing to a throttle screen layout with more possible throttles
* Cleaned up some commented out code (toast commands that have been replaced with safeToast())

Complete ChangeLog
--------------------------------------------

`view complete changelog <https://raw.githubusercontent.com/JMRI/EngineDriver/master/changelog-and-todo-list.txt>`_

