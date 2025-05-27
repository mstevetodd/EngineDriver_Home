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

Changes included in Engine Driver Beta version **2.40.199**:

* Bug fixes for the Semi-Realistic Throttle</li>
* Changed the location permission warnings to a toast message</li>
* Add option to the ED icon on the Action Bar, to return to the Throttle screen.  This will be enabled by default on new installs</li>
* Changes to the Original, Colourful and Dark themes to make the buttons more three dimensional</li>
* Rework of the Select Loco and DCC-EX screens to be more glyph based.</li>
* Rearranged the Select Loco page for better fit of non-English text. (primarily German)</li>
* New 'G' command for keyboard gamepad type to force a function even if it is momentary</li>

Changes included in Engine Driver Beta version **2.40.197**:

* When you change throttle layouts, and the new layout supports a range of throttles, Engine Driver will ask for the number.
* Send additional resync requests after DCC-EX reconnect
* DCC-EX Pref to sequence item requests
* Bug fix for F0-F9 on some systems - Removed leading zero from FKey id when sending
* Bug fix for Immersive mode
* Cleanup of the Horizontal Throttle layouts. Fixing some height issues
* only redraw Route list if actually changed
* Bug fix for Non-English 'Auto' connection protocol option
* Separate warning from when the 'Use Location' service is disabled (as different to no WiFi)

Complete ChangeLog
--------------------------------------------

`view complete changelog <https://raw.githubusercontent.com/JMRI/EngineDriver/master/changelog-and-todo-list.txt>`_

