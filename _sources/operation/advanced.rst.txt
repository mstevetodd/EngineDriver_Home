******************************************
Advanced Operation 
******************************************

.. meta::
   :keywords: Children's Timer Advanced Direction Buttons shake vibration

.. include:: ../include.rst

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
      :local:
      :depth: 3
 
Consist Follow Functions
========================

By default, in |ed|, if you activate a DCC function while controlling a Consist/Multiple Unit train only the function on the lead loco will actually be activated.
Engine Driver provides options (preferences) that will activate the functions on the other locos in the consist/multiple unit train given a number of possible rules.

The :doc:`Consist Follow Functions </operation/consist-follow-functions>` page provides information on the different rule types and how to use them.


Direction Buttons
=================

Notes:

* Direction buttons are not available on the switch/shunting throttle layouts
* The |SRT| layout (only) also includes a 'Neutral' button

.. contents:: In this Section
    :depth: 1
    :local:
    :class: in-this-section


Renaming Direction Buttons
--------------------------

Direction buttons are labelled by default as :guilabel:`Fwd` and :guilabel:`Rev` (for English), but can be renamed to anything you prefer (e.g. 'Up' and 'Down') in the preferences. 

See the :ref:`configuration/preferences:Direction Button Preferences` for information on how to change direction button labels.

Swapping Direction Buttons
--------------------------

Direction buttons are, by default shown with :guilabel:`Fwd` on the left and :guilabel:`Rev` on the right, but they can be swapped in the preferences. 

|ED| can also be configured so that a long press on either direction button will swap the buttons temporarily. This is particularly useful if you use the 'Up' and 'Down' labels, as the up/down directions mean that the loco facing can remain correct. 

See the :ref:`configuration/preferences:Direction Button Preferences` for information on how to swap the direction buttons and/or setup the long press feature.

Conserving Power 
================

If your Android device/phone runs out of battery too quickly you can try the some of the options on the :doc:`Conserving Power <../configuration/conserving_power>` page.

Children's Timer
================

|ED| provides options for time controlled running.  This was originally intended for providing a way to have children have a fair share of the use of a loco, but can be used for timed control for any purpose.

Instructions:

- Select the loco first.
- Enable the time limited running to the desired time, using either:
  
  - the `Time limited running <../configuration/preferences.html#time-limited-running>`_ preference, (then return to the |T-S|) |BR| *or* 
  - the action button (`Show Timer button? <../configuration/preferences.html#show-timer-button>`_)
  
- The timer will start with the first increase in speed
- When the timer runs out:

  - You must come back to this preference to reset the time (or clear it) |BR| *or* 
  - click the action button again.
 
Recommendations:

- Enable the Action Bar button (`Show Timer button? <../configuration/preferences.html#show-timer-button>`_)
- Disable the hardware volume keys (`Disable Volume keys? <./configuration/preferences.html#disable-volume-keys>`_)
- Disable `Swipe Through Turnouts/Points? <./configuration/preferences.html#swipe-through-turnouts-points>`_ 
- Disable `Swipe Through Routes? <./configuration/preferences.html#swipe-through-routes>`_
- Disable the `Emergency Stop button? <./configuration/preferences.html#throttle-screen-action-bar-preferences>`_

