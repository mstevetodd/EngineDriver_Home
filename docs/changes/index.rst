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

Changes included in Engine Driver Beta version **2.42.217**:

  * First version to only support Android 5 and above
  * Added preferences for action bar buttons to navigate between Throttle, Turnouts/Points and Routes
  * Added preference for medium size toolbar/action bar buttons
  * Added preference to automatically connect to a specified IP and port, even if it is not discovered
  * Added preference to start logging immediately after app startup.  Resets itself after use
  * Added preference to hide the Advanced Consist (CV19) action bar button
  * Preferences screen now shows the current value of a list or text preference without needing to open it
  * For DCC-EX automations, you are asked which loco to send on the automation. (Defaults to the currently selected loco if any.)
  * Reinstated the log and file sharing capability
  * Added XBox and VRBox Mode B gamepad types support
  * Bug fix for: gamepad calibration; gamepads with the IPLS; F11 in the keyboard gamepad 'type'
  * Visual improvements
  * Significant behind-the-scenes changes to support targetSdk 36, including enforced edge-to-edge mode
  * Various other bug fixes and code improvements

Complete ChangeLog
--------------------------------------------

`view complete changelog <https://raw.githubusercontent.com/JMRI/EngineDriver/master/changelog-and-todo-list.txt>`_
