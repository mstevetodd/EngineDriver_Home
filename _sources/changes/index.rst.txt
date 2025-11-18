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

Changes included in Engine Driver Production version **2.40.203**:

* Move to AndroidX libraries
* Support for ESU MC II/Pro
* Preference to use large toolbar buttons. Defaults to large on screens >= 6.7"/17cm.
* Bug fixes for the Semi-Realistic Throttle
* Changed the location permission warnings to a toast message
* Add option to the ED icon on the Action Bar, to return to the Throttle screen. This will be enabled by default on new installs
* Changes to the Original, Colourful and Dark themes to make the buttons more three dimensional
* Rework of the Select Loco and DCC-EX screens to be more glyph based.
* Rearranged the Select Loco page for better fit of non-English text. (primarily German)
* New 'G' command for keyboard gamepad type to force a function even if it is momentary
* When you change throttle layouts, and the new layout supports a range of throttles, Engine Driver will ask for the number.
* Send additional resync requests after DCC-EX reconnect
* DCC-EX Pref to sequence item requests
* Bug fix for F0-F9 on some systems - Removed leading zero from FKey id when sending
* Bug fix for Immersive mode
* Cleanup of the Horizontal Throttle layouts. Fixing some height issues
* Only redraw Route list if actually changed
* Bug fix for Non-English 'Auto' connection protocol option
* Separate warning from when the 'Use Location' service is disabled (as different to no WiFi)
* Fixes and changes to the Children's Timer. Added Kiosk mode option.
* New preference to send a single throttle EStop on long press of the stop button
* Added ability to share the log files, or any file from ED's scoped (private) storage
* Added ability to share any file to ED's scoped (private) storage

Beta Changes
--------------------------------------------

Changes included in Engine Driver Beta version **2.41.213**:

  * Last version of Engine Driver to support Android 4.x
  * Fix for Switching Throttle layouts going back to the connection screen
  * Rework the background notifications and restart process if the app is killed in background
  * Added preference for EStop all loco(s) on all throttles(s) when Engine Driver is pushed to background
  * Bug fix for the Power Screen when an EX-CS has one of the tracks set for AUTO
  * Removed ability to share files to ED's scoped storage. Incompatible with version Android 4.x
  * Added Preference to not beep on WiThrottle Alerts and Messages
  * Added Sort button for Recent Turnouts/Points
  * Additional buttons on the Reconnection Screen
  * Additional French translations by Alain Carasso
  * Bug fixes from the previous beta
  * Added experimental CV19 Consist tool
  * New preference to automatically connect to a named server if discovered
  * New preference for, on connection, automatically load the locos you had acquired in the previous session
  * New preference to use the WiThrottle 'd'ispatch command instead of the 'r'elease command when releasing a loco
  * Search feature added to Preferences
  * Initial Chinese translations by jsky8785

Complete ChangeLog
--------------------------------------------

`view complete changelog <https://raw.githubusercontent.com/JMRI/EngineDriver/master/changelog-and-todo-list.txt>`_
