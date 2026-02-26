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

Changes included in Engine Driver Production version **2.41.215**:

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

Beta Changes
--------------------------------------------

Changes included in Engine Driver Beta version **2.42.221**:

  * First version to only support Android 5 and above
  * Bug fixes for: multiple gamepads; gamepad calibration; gamepads with the IPLS; F11 in the keyboard gamepad 'type'
  * DCC-EX Bug fixes for: auto-connect to address and port; handoff dialog;
  * Added XBox and VRBox Mode B gamepad types support
  * Added options for action bar buttons to navigate between Throttle, Turnouts/Points and Routes
  * Added option for medium size toolbar/action bar buttons
  * Reinstated the log and file sharing capability
  * Immersive mode fixes for targetSdk 36 - enforced edge-to-edge mode
  * Added option to automatically connect to a specified IP and port, even if it is not discovered
  * Visual improvements
  * Added the missing menu items for Gamepads 4-6
  * Added localisation files for English (Singapore) and English (India)
  * Added support for the new DCC-EX EStop Pause/Resume
  * User chosen background image now applied to all common activities
  * Fix: Don't send blank rosterName to WiThrottle (caused reconnect loop)

Complete ChangeLog
--------------------------------------------

`view complete changelog <https://raw.githubusercontent.com/JMRI/EngineDriver/master/changelog-and-todo-list.txt>`_
