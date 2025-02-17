*******************************************
User Interface
*******************************************

.. meta::
   :keywords: user interface UI

.. include:: ../include.rst

----

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
      :local:
      :depth: 3

The user interface for |ED| is described and explained in these pages as 'screens'.  There are several '`Main Screens`_' which you will routinely interact with and and larger number of '`Secondary / Support Screens`_' that will interact with infrequently. 

There are also some settings that impact all of the |ED| screens, which are described towards the end of this page:

* `Theme / Styles`_
* `Localisation`_ (Language)


Main Screens
-------------

There are five main screens:

.. contents:: 
    :depth: 1
    :local:
    :class: in-this-section

Connection Screen
^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/connect.png
   :align: right

This screen is the first screen you normally see when starting |ED|. (Other than the first time you start |ED|.)

It allows you choose which |WTS-DCC-EX| to connect to, which you must do to control your trains.

There are three ways you can select a |WTS-DCC-EX| to connect to:

* `IP Address and Port`_
* `Discovered Servers`_
* `Recent Servers`_

Once you select a server the |T-S| will be automatically displayed.

If you only ever connect to one |WTS-DCC-EX| you can effectively bypass this screen by enabling the `Auto-Connect to WiThrottle Server? <../configuration/preferences.html#auto-connect-to-withrottle-server>`_ preference.

.. note:: 
  :class: note-ed-hidden-title

  See :doc:`wifi_issues` for more assistance with connection difficulties.

Connection Method Options
"""""""""""""""""""""""""

IP Address and Port
'''''''''''''''''''

  Enter the IP address or URI of the server in the first field, and the port in the second field, then click :guilabel:`Connect`. |ed| will attempt to connect to it, and the |T-S| will be displayed.

Discovered Servers
''''''''''''''''''

  This is the most common way to connect.

  Your |WTS-DCC-EX| will attempt to broadcast its details so that apps like |ED| can automatically find it.  If |ED| does find it, it will be listed here.

  To connect to any |WTS-DCC-EX| in this list, simply click on the row.  |ed| will attempt to connect to it, and the |T-S| will be displayed.

Recent Servers
''''''''''''''

  To connect to any |WTS-DCC-EX| in this list, simply click on the row.  |ed| will attempt to connect to it.  If successful the |T-S| will be displayed.

  Note that, just because it is in this list, it does not mean that you can connect to it now. It only means that you have successfully connected to it in the past.

|HR-DASHED|

Action Bar (Connection Screen)
""""""""""""""""""""""""""""""

The Action Bar appears at the top of all screens. It will show different information and different buttons depending on a\) the particular screen and b\) preferences you have set.

In the |C-S| the Action Bar only displays:

* The app name (|ed|)
 
.. note:: 
  :class: note-ed-hidden-title

  See the `Action Bar`_ section of this page for more information.

|HR-DASHED|

Overflow Menu (Connection Screen)
"""""""""""""""""""""""""""""""""

The *Overflow Menu* (or simply '*Menu*') appears in the Action Bar at the top of most of the `Main Screens`_ is normally three dots (⁞) or three bars (≡).
It will show different options depending on a) the particular screen, b) preferences you have set and c) the state of certain elements in the app.

Specific to the |C-S|, the Overflow Menu can display:

* `Preferences <../configuration/preferences.html>`_
* `View Log <../operation/interface.html#view-log-screen>`_
* `Exit <../operation/operation.html#exiting-engine-driver>`_
* `About <../operation/interface.html#about-screen>`_

.. note:: 
   :class: note-ed-hidden-title

   See the `Overflow Menu`_  section for more information.

----

Throttle Screen
^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/throttle_vertical_outline.png
   :scale: 8 %
   :align: right

The |T-S| has two distinct areas:

* The Action Bar
* One or more Throttle Areas

There are also some settings that impact the whole |T-S| which described towards the end of this section:

* Background
* Immersive Mode (Full Screen)
* Swipe Up / Down
* Accelerometer (Shake)  
 
The |T-S| allows you to control:

- Access common functions from the Action Bar and Menu
- Control one or more locos

The |T-S| contains between 1 and 6 Throttle areas depending on the :ref:`Throttle layout <configuration/preferences:throttle screen layout>` chosen and the number of throttles for that layout (only some allow this to be changed).  

|HR-DASHED|

Throttle Area
""""""""""""""""""""""""""""""""""""

.. image:: ../_static/images/parts/throttle_area1.png
   :scale: 10 %
   :class: align-right

Each Throttle on the |T-S| will display different information and buttons depending on the ``Throttle Screen Layout`` in the  :ref:`Throttle Screen Layout <configuration/preferences:throttle screen layout>` preference.


Each *Throttle Area* allows you to:

* Select and release locos 
* Control the speed and direction of your trains
* Activate DCC decoder functions like the light, bell, horn 
* Activate Virtual (IPLS) Sounds (bell, horn, short horn) (if enabled)

.. image:: ../_static/images/parts/throttle_area2.png
   :scale: 10 %
   :class: align-right

.. contents:: In this Section
    :depth: 1
    :local:
    :class: in-this-section

|HR-DASHED|

Loco Select Button
''''''''''''''''''''''''''''''''

The loco :guilabel:`Select` button in the Throttle Area allows to select or release locos for that particular Throttle.  Click on the button and you will be taken to the Select Loco screen.

Once you have selected a loco, the label on the button will change to the DCC Address(s) or the |ROSTER| name(s) of the Loco depending on how you selected the loco in the |LS-S|, and if you have the enabled the :ref:`Loco Address instead of Name? <configuration/preferences:loco address instead of name?>` preference.

When the button is displaying DCC Address(s) or the |ROSTER| name(s), click on the button again and you will be taken to the |LS-S| where you can de-select the loco(s), select additional locos to make a |consist| train, edit the locos in the consist, or edit the lights of the locos in the |consist|.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Operation <operation/operation:Selecting & Releasing Locos>` page for more information.

|HR-DASHED|

Speed indicator
''''''''''''''''''''''''''''''''

The *Speed Indicator* or *Speed* area of each throttle of the |T-S| indicates the throttle amount/setting (rather than the actual speed of the locos controlled by the the throttle).

Depending on the :ref:`Speed Units Preference <configuration/preferences:speed units>` the upper limit shown will be different: 

.. list-table::
  :width: 100%
  :widths: 60 20 20
  :header-rows: 1

  * - Speed Unit Setting
    - Low value
    - High Value
  * - Percent 0 - 100% 
    - 0
    - 100
  * - Auto Speed steps 
    - ?
    - ?
  * - 8 steps 
    - 0
    - 8
  * - 10 steps 
    - 0
    - 10
  * - 14 steps 
    - 0
    - 14
  * - 28 steps 
    - 0
    - 28
  * - 128 steps
    - 0
    - 128

Also, if one of the :ref:`Shunting/Switching layouts <configuration/preferences:throttle screen layout>` is selected, the high number will be negative ('-') when reversed (e.g. -100 - 0 - 100)

The *Speed Indicator* area also can show:

* Volume indicator
* Gamepad Indicator
* Direction indicator (Shunting/Switching Layouts only)

*Volume Indicator*

A 'V' will be shown in the *Speed Indicator* area to indicate which throttle is being controlled by the hardware volume buttons.
Touch another *Speed Indicator* to change which Throttle the Hardware Volume buttons control.

*Gamepad Indicator*

A number ('1','2', etc.) will be shown in the *Speed Indicator* area to indicate which throttle is being controlled by the each connected gamepad.  Set one of the gamepads to allow you to switch throttle it controls.

*Direction Indicator*

If one of the Shunting/Switching layouts is selected, a triangle symbol will be shown to indicate direction (pointing Up for forward, and down for reverse).

.. note:: 
  :class: note-ed-hidden-title

  See the Throttle Control Preferences section of the :ref:`Speed Units preference <configuration/preferences:speed units>` for a information on changing the ``Speed Units`` options.

|HR-DASHED|

Speed Slider Area
'''''''''''''''''
.. image:: ../_static/images/parts/slider_horizontal.png
  :scale: 100 %

The Throttle areas can be configured to have a *Speed Slider*.  (All :ref:`Throttle Screen Layouts <configuration/preferences:throttle screen layout>` except the 'Big Button' layouts include sliders by default.) 

**Dragging you finger** along the slider will increase or decrease the speed of the loco(s) selected for the that Throttle. 

**Pressing and holding** your finger at one spot on the slider will cause |ED| to slowly increase or decrease the speed of the loco(s) selected for that Throttle till it gets to that point.

Depending on the ``Throttle Screen Layout`` chosen in the  :ref:`Throttle Screen Layout <configuration/preferences:throttle screen layout>` preference, all sliders on the |T-S| will be either:

* one-directional (0% - 100%) [#PCT]_  |BR|\ or 
* bi-directional (-100% - 0 - +100%) |BR| |BR|

Bi-directional sliders are useful for when you are switching/shunting. i.e. moving your locos backwards and forwards a lot.

Several preferences can change the appearance or actions of the *Speed Slider*\:

* :ref:`Increase Slider/Speed Height? <configuration/preferences:increase slider/speed height?>` |BR| When set, this preference will show a taller Slider, or Speed buttons, for throttles
* :ref:`Throttle Speed Slider Margin <configuration/preferences:throttle speed slider margin>` |BR| When set, this changes the space between either the edge of the screen and the ends of the Slider, or if the Speed Buttons are enabled, the edge of the Speed Buttons and the ends of the Slider. Specific in pixels haw far to offset
* :ref:`Hide Speed Slider? <configuration/preferences:hide speed slider?>` |BR| When this preferences is set, |ed| will not show speed slider, use speed buttons instead
* :ref:`Tick Marks on Speed Sliders? <configuration/preferences:tick marks on speed sliders?>` |BR| When this preferences is set, |ED| will show tick marks on the background of the Speed Sliders
* :ref:`Switching throttle Dead Zone <configuration/preferences:switching throttle dead zone>` |BR| When this preferences is set, |ED| will set the size of the dead zone, or detent, on the slider of the Switching/Shunting |T-S|
* :ref:`Stop Button Vertical Margins <configuration/preferences:stop button vertical margins>` |BR| When this preferences is set, |ED| will add the entered number of pixels to offset margins of the stop button from the speed buttons and bottom of screen

.. [#PCT] The actual amounts shown in the *Speed Indicator* will depend on the ``Speed Units`` chosen in the :ref:`Speed Units preference <configuration/preferences:speed units>`.

|HR-DASHED|

Stop Button
''''''''''''''''''''''''''''''''

.. image:: ../_static/images/parts/stop_button_horizontal.png
   :scale: 80 %

Clicking the ``Stop`` button of a throttle will the |loco_consist| controlled by that throttle.  If the locos have momentum configured in the decoder it/they will come slowly to a stop.  i.e. it obeys the momentum CV settings.

.. note:: 
  :class: note-ed-hidden-title

  See the `Emergeny Stop Action Bar button <emergency stop button>`_ for information on stopping locos immediately, overriding the momentum setting.

|HR-DASHED|

Speed Buttons
''''''''''''''''''''''''''''''''

.. image:: ../_static/images/parts/speed_buttons_horizontal.png
  :scale: 100 %

The Throttles may optionally be configured have simple buttons that allow you to increase or decrease the loco's speed in pre-defined steps. 

For horizontal *speed sliders*, the buttons are displayed at the left and right ends of the sliders. For vertical *speed sliders*, the buttons are displayed at the top and bottom of the sliders.

When enabled:

* The :guilabel:`++` or :guilabel:`>>` will **increase** the throttle speed by the :ref:`Speed Button Change Amount <configuration/preferences:speed button change amount>`.
* The :guilabel:`- -` or :guilabel:`<<` will **decrease** the throttle speed by the :ref:`Speed Button Change Amount <configuration/preferences:speed button change amount>`.

For the Horizontal Sliders only, The position of these buttons in relation to the speed sliders (the space between), can be altered with the :ref:`Speed Slider Margin <configuration/preferences:throttle speed slider margin>` preference.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Display Speed Buttons? <configuration/preferences:display speed buttons?>` preference for more information on enabling these buttons.

  See the :ref:`Speed Button Change Amount <configuration/preferences:speed button change amount>` preference for information on the about these buttons. 

|HR-DASHED|

Direction Buttons Area
'''''''''''''''''''''''

.. image:: ../_static/images/parts/direction_buttons.png
  :scale: 80 %

Each Throttle on the |T-S| will display :guilabel:`Forward` and :guilabel:`Reverse` direction buttons, depending on the ``Throttle Screen Layout`` in the  :ref:`Throttle Screen Layout <configuration/preferences:throttle screen layout>` preference.  'Shunting/Switching' layouts do not show the direction buttons.

Change direction while moving preference.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Direction change while moving? <configuration/preferences:direction change while moving?>`  and :ref:`Stop on Direction change? <configuration/preferences:stop on direction change?>` preferences for information on preferences which alter when the buttons are available and the way the they work.

|HR-DASHED|

Function Buttons Scroll Area
''''''''''''''''''''''''''''

The *Function Buttons Scroll Area* will show form 0 (zero) to 26 function buttons depending on a number of factors. Each button will show either:

* Labels provided from the |ROSTER|, which can be individually specified for each loco in the |ROSTER|
* The default labels for |ed|  (which can be changed)

The *Function Button area* can also show:

* IPLS buttons  (In Phone Loco Sounds)
* Pause
* Limit Speed

The *Function Buttons Scroll Area* is shown by default on all Throttle Screen layouts except ``Simple``.  It can be enable for the ``Simple`` layout

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Function Button Area Size <configuration/preferences:function buttons area size>` preference for information on how to show the *Function Button Scroll Area* on the simple layout.

|HR-DASHED|

DCC Function buttons
''''''''''''''''''''

.. todo:: 
  :class: todo-float-right
  
  MEDIUM: DCC Function buttons

DCC Function Buttons are displayed here.  If there are too many to display in the screen area allocated, then the area becomes scrollable (without scroll bars) so that they can all be viewed and pressed as needed.  

All throttle layouts other than the 'Simple' layout show a *Function Buttons Scroll Area* by default.  For the 'Simple' layout it must be enable in the preferences if required.

Will show from 0 (zero) to 26 DCC function buttons, depending on a number of factors. Each button will show either:

* Labels provided from the |ROSTER|, which can be individually specified for each loco in the |ROSTER|
* The default labels for |ed|  (which can be changed)


If the loco (or first loco of a |consist|) was selected from the |WTS-DCC-EX| |ROSTER|, then (by default) the number of functions and labels on the buttons will be whatever is configured for that loco in the |WTS-DCC-EX|.  This is also turn if the loco is selected from the Recent Locos list or the Recent |consists| list.

If the loco (or first loco of a |consist|) was added by entering its DCC Address, then the number of functions and labels on the buttons will be whatever is configured in |ED| in the |FD-S|.

The behaviour of the Function Buttons for locos selected from the |WTS-DCC-EX| |ROSTER| can be overridden with the :ref:`Use default function labels? <configuration/preferences:use default function labels?>` preference.  If this is enabled, the locos selected from the |WTS-DCC-EX| |ROSTER| will also show the Default Functions labels.

Clicking on any function button will instruct the loco to activate that DCC Function in the loco.  By default this is only sent to the Lead loco, however this can be overridden in a number of different ways.

.. note:: 
  :class: note-ed-hidden-title

  See the `Function Defaults Screen <Function Defaults Screen>`_ section for more information on configuring the labels and number of *default function* buttons.

  See the :doc:`Function Buttons </configuration/functions>` page for more information on the DCC Function buttons.

  For labels from |ROSTER| Entries you need to edit the Function buttons in the |WTS-DCC-EX|, or configure |ed| to use the default labels.

|HR-DASHED|

Pause and Limit Speed buttons
'''''''''''''''''''''''''''''

.. image:: ../_static/images/parts/limit_speed_and_pause_buttons.png
  :scale: 20 %
  :class: align-right

The *Function Button area* can also show:
* *Pause* button
* *Limit Speed* button

These are optional buttons that, if enabled, appear in the same areas as the Function Buttons and the :doc:`In Phone Loco Sounds buttons </configuration/ipls>` (if enabled).

**Pause Button** 

When clicked while the |loco_consist| is moving, the :guilabel:`Pause` button will gradually slow the train down zero and a predefined rate.  The rate can be altered in the preferences.

When subsequently clicked while the |loco_consist| is stationary, the :guilabel:`Pause` button will gradually increase the speed of the train till it is at the speed that it was at when the button was first pressed. i.e. its original speed.

**Alternate Pause Button** 

An 'alternate Pause button' can be enabled in the preferences.  This behaves exactly the same as the normal Pause button, but appears below the throttle slider and speed buttons.

**Limit Speed Button** 

When enabled by clicking on the :guilabel:`Limit Speed` button, |ED| will restrict the maximum speed on the throttle to the predefined amount.  By default the speed will be 50%, but this can be changed in preferences.

  .. note:: 
    :class: note-ed-hidden-title

    See the :ref:`'Limit Speed' & 'Pause' button Preferences <configuration/preferences:'Limit Speed' & 'Pause' button Preferences>` section on the Preferences page for more information on these buttons.

|HR-DASHED|

In Phone Loco Sounds buttons (IPLS)
'''''''''''''''''''''''''''''''''''

The *Function Button area* can also be configured in the preferences to show the IPLS buttons  (In Phone Loco Sounds)

These are optional buttons that allow you to 'play' specific loco related sounds through your device/phone.

The buttons include:

* Mute
* Bell
* Horn
* Short Horn

'Horn' and 'Short Horn' are momentary.  'Mute' and 'Bell' are latching.

'Mute' can be hidden by changing a preferences.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`operation/operation:virtual sounds - in phone loco sounds (ipls)` section of the operation page for more information using the IPLS.

  See the :doc:`In Phone Loco Sounds (IPLS) </configuration/ipls>` page for more information on the configuring IPLS buttons.

|HR-DASHED|

Load Slider Area
''''''''''''''''

This is unique to the |SRT-TS|.

The 'Load' slider is intended to simulate if the train you are controlling has none, a few, many, or a huge number of carriages behind it. Load can also be increased or decreased to simulate going up or down a slope.

The Load can be set to show either a percentage slider or a slider with a distinct number of steps/notches.

The maximum load can be set in the preferences. (the Default is 1000%) The Load slider is exponential in scale, so from notch 0 to 1 to 2 only small increases of load are applied, but by the final notches, huge changes are applied.

Refer to the :doc:`/operation/semi-realistic-throttle` page for more information.

|HR-DASHED|

Brake Slider Area
'''''''''''''''''

This is unique to the |SRT-TS|.

The 'Air Brake' feature is designed to simulate a very rough approximation of the Westinghouse Air Brake system used by early US railroads.

The Brake slider can be used with or without the simulation of the Air Reservoir and Air Line.

Refer to the :doc:`/operation/semi-realistic-throttle` page for more information.

|HR-DASHED|

Web View Area (Throttle Web View)
"""""""""""""""""""""""""""""""""
   
.. todo:: 
  :class: todo-float-right
  
  LOW: Web View Area (Throttle Web View)

Optional, shows a web browser in the lower half of the |T-S|.

Your JMRI Layout panels can be displayed here if you have configured them in JMRI. 

Anything that can be shown in the `Web View Screen`_ can equally be shown here, just in a smaller space.

.. note:: 
  :class: note-ed-hidden-title

  see preference

  see initial page preference

  different to the main `Web View Screen`_ including a different preference to set the initial page.

  see increase size

|HR-DASHED|

Action Bar (Throttle Screen)
""""""""""""""""""""""""""""

.. image:: ../_static/images/parts/action_bar.png
  :align: right
  :scale: 33%

The Action Bar appears at the top of all screens. It will show different information and different buttons depending on a\) the particular screen and b\) preferences you have set.

In the |T-S| the Action Bar can display:

* The app name (|ed|)
* Optionally configured information:

  * Fast Clock
  * Children's Timer Status and Countdown
  * Full Screen or Action Bar Only left/right swipe
  * |WTS-DCC-EX| Name

* Optionally configured buttons:

  * Emergency Stop  (EStop)
  * Track Power
  * Flashlight
  * Throttle Web View
  * Throttle Layout Switching
  * In Phone Loco Sound
  * Children's Timer

.. note:: 
   :class: note-ed-hidden-title

   The optional action bar buttons are enabled via the :menuselection:`Menu --> Preferences --> Throttle Screen Status Row Preferences`.  
    
   See the `Action Bar`_ section of this page for more information.

|HR-DASHED|

Overflow Menu (Throttle Screen)
"""""""""""""""""""""""""""""""

.. image:: ../_static/images/parts/menu_throttle.png
  :align: right
  :scale: 33%

The *Overflow Menu* (or simply '*Menu*') appears in the Action Bar at the top of most of the `Main Screens`_ is normally three dots (⁞) or three bars (≡).
It will show different options depending on a) the particular screen, b) preferences you have set and c) the state of certain elements in the app.

Specific to the |T-S|, the Overflow Menu can display:

* `Turnouts/Points Screen`_ (All except the *Turnout/Points Screen* only)
* `Routes Screen>` (All except the |R-S| only)
* `Function Defaults Screen`_ (|T-S| only)
* Gamepads (|T-S| only)

  * `Gamepad Test 1 <Gamepad Test Screen>`_
  * `Gamepad Test ... <Gamepad Test Screen>`_

* :ref:`Loco Sounds <operation/interface:in phone loco sounds screen>` (|T-S| only)
* `DCC-EX Screen`_ (If connected to a DCC-EX EX-CommandStation using the |NATIVE| only)
* `DCC-EX Function Settings Screen`_ (If connected to a DCC-EX EX-CommandStation using the |NATIVE| only)
* :ref:`Power <operation/operation:turn track power on>`
* :doc:`Preferences </configuration/preferences>`
* :ref:`View Log <operation/interface:view log screen>`
* :ref:`Exit <operation/operation:exiting engine driver>`
* :ref:`About <operation/interface:about screen>`




.. note:: 
  :class: note-ed-hidden-title

  See the `Overflow Menu`_  section for more information.

.. image:: ../_static/images/screenshots/background_fill.png
  :align: right
  :scale: 12%

|HR-DASHED|

Background
""""""""""

|ed| can show a background image of your choosing on the |T-S|.  Any image/photo on your device/phone can be used.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Background Images section <configuration/preferences:background image preferences>` of the preferences for more information on how to select a background image.

|HR-DASHED|

Immersive Mode (Full Screen)
""""""""""""""""""""""""""""

.. todo:: 
  :class: todo-float-right
  
  MEDIUM: Immersive Mode (Full Screen)

Immersive mode hides the system navigation buttons at the bottom of the screen on the Throttle screen only, to give you more screen real estate for the throttle UI.

It can optionally also hide the Android System Status Bar at the top of the page.

Swiping up from off screen will normally temporarily show the Android navigation buttons again.

You can also configure specific :ref:`Swipe up or Swipe down <configuration/preferences:swipe up-down preferences>` or :ref:`Shake <configuration/preferences:accelerometer (shake) preferences>` preferences to enter or exit immersive mode.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`configuration/preferences:Swipe Up-Down Preferences` for more information on how to configure immersive mode.

|HR-DASHED|

Swipe Left / Right (From Throttle)
""""""""""""""""""""""""""""""""""

Swiping Left from the |T-S| will take you to the `Routes Screen`_, unless it has been disabled in the preferences

Swiping Right from the |T-S| will take you to the `Turnouts/Points Screen`_, unless it has been disabled in the preferences

By default, you can Left/Right Swipe from any part of the screen, but this can be changed to just the Action Bar in the preferences. This can be useful if Left/Right swipes in the |WV-S| and *Throttle Web view* causes problems. 

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Left/right swipe preferences <configuration/preferences:left/right swipe preferences>` for information on how to enable and disable which screens are in the Left / Right swipe sequence.

  See the :ref:`Disable Full Screen Swipe prefernce <configuration/preferences:disable full screen swipe?>` to enable or disable the Swipe Action Bar only option.

|HR-DASHED|

Swipe Up / Down
"""""""""""""""

Swiping Up and/or Down on the Throttle page can optional be configured to:

* Do Nothing
* Hide the Web View (if enabled)
* Lock and Dim the screen
* Dim the screen
* Enable/Disable Immersive mode
* Switch Throttle Layouts
* Increase/Decrease Loco speed
* Go to the next throttle

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Swipe Up/Down preferences <configuration/preferences:swipe up-down preferences>` for information on how to configure what the up and down swipes do.

|HR-DASHED|

Accelerometer (Shake)  
"""""""""""""""""""""

Shaking your device/phone while on the Throttle page can optional be configured to:

* Do Nothing
* Hide the Web View (if enabled)
* Lock and Dim the screen
* Dim the screen
* Switch Throttle Layouts
* Go to the next throttle

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Accelerometer (Shake) preferences <configuration/preferences:accelerometer (shake) preferences>` for information on how to configure what the Accelerometer (Shake) do.

Turnouts/Points Screen
^^^^^^^^^^^^^^^^^^^^^^

Accessed from any of the `Main Screens`_ by the :menuselection:`Menu --> Turnouts`` or :menuselection:`Menu --> Points` or by swiping right from the Throttle Screen if enabled in the Left with the ``Swipe through Turnouts?`` or ``Swipe through Points?`` preference: :menuselection:`Menu --> Preferences --> Left/Right Swipe Preferences --> Swipe through Turnouts/Points`

This screen allows you to display all Turnouts/Points that have been defined in JMRI.

*Turnouts/Points* can be operated three ways:

* By entering the DCC Address
* From the Defined Turnout/Point list provided by the |WTS-DCC-EX| (JMRI)
* From the Recent Turnout/Point list

Turnouts/Points can be changed from 'Closed' to 'Thrown' and vice versa be pressing on either the :guilabel:`Closed` or :guilabel:`Thrown` buttons

.. image:: ../_static/images/screenshots/turnouts_jmri.png
  :align: right
  :scale: 8%

**Via the list from Server**

By selecting the 'JMRI Defined' radio button, |ED| will show the Turnouts/Points defined in the |SERVER|.

Click on the button(s) on the beside the entry to :guilabel:`Throw`` or :guilabel:`Close` the Turnout/Point.

Note:

* If the Turnout/Point button says 'Thrown', then clicking on the button will **'Close'** the Turnout/Point and the button will then say 'Closed'.
* If the Turnout/Point button says 'Closed', then clicking on the button will **'Throw'** the Turnout/Point and the button will then say 'Thrown'.

.. note:: 
  :class: note-ed-hidden-title

  Note that this list can optionally be set to *always* show :guilabel:`Close` and :guilabel:`Throw` rather than :guilabel:`Closed` or :guilabel:`Thrown` by setting the :ref:`configuration/preferences:Always Show Throw/Close?` preference.

|FORCE-BREAK|

.. image:: ../_static/images/screenshots/turnouts_entry.png
  :align: right
  :scale: 8%

**By Entering an Address**

By selecting the 'Address/Recent' radio button, |ED| will allow you to throw/close any arbitrary Turnout/Point.

Enter the address of the Turnout/Point and press any of the buttons:

* :guilabel:`Throw`
* :guilabel:`Close`
* :guilabel:`Toggle`

**Recent**

By selecting the 'Address/Recent' radio button, |ED| will allow you to throw/close any recently used Turnout/Point.

Click on the buttons on the beside the entry to 'Throw' or 'Close' the Turnout/Point.

|FORCE-BREAK|

**Filter by location**

The 'Turnout/Points List' can be filtered.  The filtering relies on the idea that the first part of every Turnout/Point name is a 'Location', followed by a common separator, then the actual name for the Turnout/Point name.  The 'filter' then allows you to select one of those locations and |ed| can just show the Turnout/Points at the 'Location'.

The :ref:`Location Delimiter <configuration/preferences:location delimiter>` preference allows you to set the character that marks the end of the Location portion of Turnout/Point and Route names.  By default it is a colon (":") but any character can be used.


.. note:: 
  :class: note-ed-hidden-title

  A number of preferences can alter the way Turnouts/Points are displayed. See :ref:`configuration/preferences:Turnouts/Points and Routes Preferences` for more information.

|HR-DASHED|

Action Bar (Turnouts/Points Screen)
"""""""""""""""""""""""""""""""""""

.. image:: ../_static/images/parts/action_bar.png
  :align: right
  :scale: 33%

The Action Bar appears at the top of all screens. It will show different information and different buttons depending on a\) the particular screen and b\) preferences you have set.

In the |TP-S| the Action Bar can display:

* The app name (|ed|)
* Optionally configured information:

  * Fast Clock
  * Full Screen or Action Bar Only left/right swipe
  * |WTS-DCC-EX| Name

* Optionally configured buttons:

  * Emergency Stop  (EStop)
  * Track Power
  * Flashlight

.. note:: 
  :class: note-ed-hidden-title

  The optional buttons are enabled via the :menuselection:`Menu --> Preferences --> Throttle Screen Status Row Preferences`.  
  
  See the `Action Bar`_ section of this page for more information.

|HR-DASHED|

Overflow Menu (Turnouts/Points Screen)
""""""""""""""""""""""""""""""""""""""

The *Overflow Menu* (or simply '*Menu*') appears in the Action Bar at the top of most of the `Main Screens`_ is normally three dots (⁞) or three bars (≡).
It will show different options depending on a) the particular screen, b) preferences you have set and c) the state of certain elements in the app.

Specific to the *Turnouts/Points  Screen*, the Overflow Menu can display:

* `Throttle Screen`_ (All except the |T-S| only)
* `Routes Screen`_ (All except the |R-S| only)
* `DCC-EX Screen`_ (If connected to a DCC-EX EX-Command-Station using the |NATIVE| only)
* `DCC-EX Function Settings Screen`_ (If connected to a DCC-EX EX-CommandStation using the |NATIVE| only)
* :ref:`Power <operation/operation:turn track power on>`
* :doc:`Preferences </configuration/preferences>`
* :ref:`View Log <operation/interface:view log screen>`
* :ref:`Exit <operation/operation:exiting engine driver>`
* :ref:`About <operation/interface:about screen>`


.. note:: 
  :class: note-ed-hidden-title

  See the `Overflow Menu`_  section for more information.

|HR-DASHED|

Swipe Left / Right (From Turnouts/Points)
"""""""""""""""""""""""""""""""""""""""""

Swiping Left from the |TP-S| will take you to the `Throttle Screen`_, unless it has been disabled in the preferences

Swiping Right from the |T-S| will take you to the `Web View Screen`_, unless it has been disabled in the preferences

By default, you can Left/Right Swipe from any part of the screen, but this can be changed to just the Action Bar in the preferences. This can be useful if Left/Right swipes in the |WV-S| and *Throttle Web view* causes problems. 

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Left right swipe preferences <configuration/preferences:left/right swipe preferences>` for information on how to enable and disable which screens are in the Left / Right swipe sequence.

  See the :ref:`Disable Full Screen Swipe prefernce <configuration/preferences:disable full screen swipe?>` to enable or disable the Swipe Action Bar only option.

Routes Screen
^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/routes.png
  :align: right
  :scale: 8%

Accessed from any of the `Main Screens`_ by the menu :menuselection:`Menu --> Routes` or by swiping left from the Throttle Screen if enabled in the Left with the ``Swipe through Routes?`` preference: :menuselection:`Menu --> Preferences --> Left/Right Swipe Preferences --> Swipe through Routes`

This screen displays all Routes that have been defined in your |SERVER| and allows you to activate them.

**By System name**

You can enter the route ID and click :guilabel:`Set` button to activate a route.

**Via the List from the Server**

You can select the route from the list provider by your |SERVER|...

Click on the :guilabel:`Set` buttonon the beside the entry to activate the Route.

Note, When using the |native| the |EX-CS| (only) can:

* dynamically change the label on the the button
* dynamically show or hide Routes
* dynamically enable or disable Routes

**Filter by location**

The 'Routes List' can be filtered.  The filtering relies on the idea that the first part of every Route name is a 'Location', followed by a common separator, then the actual name for the Route name.  The 'filter' then allows you to select one of those locations and |ed| can just show the Routes at the 'Location'.

The :ref:`Location Delimiter <configuration/preferences:location delimiter>` preference allows you to set the character that marks the end of the Location portion of Turnout/Point and Route names.  By default it is a colon (":") but any character can be used.

.. note:: 
  :class: note-ed-hidden-title

  A number of preferences can alter the way Routes are displayed. See :ref:`configuration/preferences:Turnouts/Points and Routes Preferences` for more information.

|HR-DASHED|

Action Bar (Routes Screen)
""""""""""""""""""""""""""

.. image:: ../_static/images/parts/action_bar.png
  :align: right
  :scale: 33%

The Action Bar appears at the top of all screens. It will show different information and different buttons depending on a\) the particular screen and b\) preferences you have set.

In the |R-S| the Action Bar can display:

* The app name (|ed|)
* Optionally configured information:

  * Fast Clock
  * Full Screen or Action Bar Only left/right swipe
  * |WTS-DCC-EX| Name

* Optionally configured buttons:

  * Emergency Stop  (EStop)
  * Track Power

.. note:: 
  :class: note-ed-hidden-title

  The optional buttons are enabled via the :menuselection:`Menu --> Preferences --> Throttle Screen Status Row Preferences`.  
  
  See `Action Bar`_ section of this page for more information.

|HR-DASHED|

Overflow Menu (Routes Screen)
"""""""""""""""""""""""""""""

The *Overflow Menu* (or simply '*Menu*') appears in the Action Bar at the top of most of the `main screens <../operation/interface.html#main-screens>`_ is normally three dots (⁞) or three bars (≡).
It will show different options depending on a) the particular screen, b) preferences you have set and c) the state of certain elements in the app.

Specific to the |R-S|, the Overflow Menu can display:

* `Throttle Screen`_ (All except the |T-S| only)
* `Turnouts/Points Screen`_ (All except the *Turnout/Points Screen* only)
* `DCC-EX Screen`_ (If connected to a DCC-EX EX-Command-Station using the |NATIVE| only)
* `DCC-EX Function Settings Screen`_ (If connected to a DCC-EX EX-CommandStation using the |NATIVE| only)
* :ref:`Power <operation/operation:turn track power on>`
* :doc:`Preferences </configuration/preferences>`
* :ref:`View Log <operation/interface:view log screen>`
* :ref:`Exit <operation/operation:exiting engine driver>`
* :ref:`About <operation/interface:about screen>`


.. note:: 
   :class: note-ed-hidden-title

   See the `Overflow Menu`_  section for more information.

|HR-DASHED|

Swipe Left / Right (From Routes)
""""""""""""""""""""""""""""""""

Swiping Left from the |R-S| will take you to the `Web View Screen`_, unless it has been disabled in the preferences

Swiping Right from the |R-S| will take you to the `Throttle Screen`_, unless it has been disabled in the preferences

By default, you can Left/Right Swipe from any part of the screen, but this can be changed to just the Action Bar in the preferences. This can be useful if Left/Right swipes in the |WV-S| and *Throttle Web view* causes problems. 

.. note:: 
  :class: note-ed-hidden-title

  See the `Left right swipe preferences <./configuration/preferences.html#left-right-swipe-preferences>`_ for information on how to enable and disable which screens are in the Left / Right swipe sequence.

  See the `Disable Full Screen Swipe prefernce <configuration/preferences.html#disable-full-screen-swipe>`_ to enable or disable the Swipe Action Bar only option.

----

Web View Screen
^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/web_view_screen.png
  :align: right
  :scale: 12%

.. image:: ../_static/images/screenshots/web_view_screen2.png
  :align: right
  :scale: 12%

Accessed from any of the main screens by the menu :menuselection:`Menu --> Web` or by swiping left or right twice from the |T-S| if enabled in the Left with the ``Swipe through Web?`` preference: :menuselection:`Menu --> Preferences --> Left/Right Swipe Preferences --> Swipe through Web`
It can also be accessed, if the ``Screen orientation`` preference is set to ``Auto Web``, by rotating the Android Device/Phone.

This screen displays a web browser interface that lets you view any web page. Normally this will be a web page on your JMRI server. 

.. todo:: 
  :class: todo-float-right
  
  MEDIUM: Web View Screen
  
From the JMRI web server you can view and interact with additional features of JMRI.  The menu at the top right of the web panel screen allows you to further display:

* Rosters
* Operations
* Trains
* Tables
* Turnouts/Points
* Sensors
* Routes
* Reporters
* Memories
* Blocks
* Layout Blocks
* Lights
* Signal Masts
* Signal Heads
* Locations
* Cars
* Engines
* ID Tags

This can be used for:

* A webThrottle screen
* Your JMRI layout panel(s)
* Any URL in a full screen.  This is in addition to being able to display your JMRI layout panel in a small section of the main |T-S|.

Tap on any of the Open Windows to expand its view.  You can then resize the panel by pinching and zooming.  It is sometimes useful to rotate your device to landscape mode, so as to better view your layout.

|HR-DASHED|

Action Bar (Web View Screen)
""""""""""""""""""""""""""""

.. image:: ../_static/images/parts/action_bar.png
  :align: right
  :scale: 33%

The Action Bar appears at the top of all screens. It will show different information and different buttons depending on a\) the particular screen and b\) preferences you have set.

In the |WV-S| the Action Bar can display:

* The app name (|ed|)
* Optionally configured information:

  * Fast Clock
  * Full Screen or Action Bar Only left/right swipe
  * |WTS-DCC-EX| Name

* Optionally configured buttons:

  * Emergency Stop  (EStop)
  * Track Power

.. note:: 
   :class: note-ed-hidden-title

   The optional buttons are enabled via the :menuselection:`Menu --> Preferences --> Throttle Screen Status Row Preferences`.  
    
   See `Action Bar`_ section of this page for more information.

|HR-DASHED|

Overflow Menu (Web View Screen)
"""""""""""""""""""""""""""""""

The *Overflow Menu* (or simply '*Menu*') appears in the Action Bar at the top of most of the `main screens <../operation/interface.html#main-screens>`_ is normally three dots (⁞) or three bars (≡).
It will show different options depending on a) the particular screen, b) preferences you have set and c) the state of certain elements in the app.

Specific to the |WV-S|, the Overflow Menu can display:

* :ref:`Throttle <operation/interface:throttle screen>` (All except the |T-S| only)
* :ref:`Turnouts/Points <operation/interface:turnouts/points screen>` (All except the *Turnout/Points Screen* only)
* :ref:`Routes <operation/interface:routes screen>` (All except the |R-S| only)
* :ref:`Power <operation/operation:turn track power on>`
* :doc:`Preferences </configuration/preferences>`
* :ref:`View Log <operation/interface:view log screen>`
* :ref:`Exit <operation/operation:exiting engine driver>`
* :ref:`About <operation/interface:about screen>`

.. note:: 
  :class: note-ed-hidden-title

  See the `Overflow Menu`_  section for more information.

|HR-DASHED|

Swipe Left / Right (Web View Screen)
""""""""""""""""""""""""""""""""""""

.. todo:: 
  :class: todo-float-right
  
  LOW: Swipe Left / Right (Web View Screen)

|FORCE-BREAK|

Secondary / Support Screens
-------------------------------

The follow additional screens will be shown at different times and for various reasons: 

.. contents:: 
    :depth: 1
    :local:
    :class: in-this-section

Intro/Setup Wizard Screen
^^^^^^^^^^^^^^^^^^^^^^^^^

The *Setup Wizard* will start automatically the first time you run |ed| after you install it.  It sets some basic preferences and asks for the necessary permissions.  These preferences can be subsequently be changed use the : :menuselection:`Menu --> Preferences`, or by re-running the wizard, which can only be done from the menu on the |C-S|.

.. note:: 
  :class: note-ed-hidden-title

  See the  :doc:`Setup wizard page </configuration/setup_wizard>`  for more information.

Loco Select Screen
^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/select_roster_existing_consist.png
  :align: right
  :scale: 12%

The |LS-S| allows you add locos to a (one of) throttle on the |T-S|.  It also provides access to the additional screens for 'Editing the Consist', 'Editing Lights' and editing the 'In Phone Locos Sounds'.

The |LS-S| is only shown when you click a :guilabel:`Select` button on the |T-S|.

Not that the :guilabel:`Select` button will should the Address(es) or the Name(s) of a|loco_consist| Train only the first loco is selected.  Click on the button will (while it is in this state) will again take to this screen to allow to you add additional Locos to the |consist| Train, or make other changes to the |consist| Train.

Selection Method
""""""""""""""""

There are four ways you can choose a loco for the Throttle.  Select one of the radio buttons depending on how you want to the choose the loco:

* DCC Address
* Server Roster
* Recent Locos
* Recent Consists

Select by DCC Address 
"""""""""""""""""""""

.. todo:: 
  :class: todo-float-right
  
  MEDIUM: Select by DCC Address

Shown if you select ``DCC Address`` in the `Selection Method`_.

You can enter the loco's DCC address (verify short or long), and press :guilabel:`Acquire` to select the loco.  You will then be taken back to the |T-S| with that loco selected.

Select from Sever Roster
""""""""""""""""""""""""

Shown if you select ``Server Roster`` in the `Selection Method`_.

If the loco you want to control is in the list, simply click on it and you will be taken back to the |T-S| with that loco selected.

For this to be possible, the Loco you want to control needs to be in the |ROSTER| of the |WTS-DCC-EX|.  Not all |WTS-DCC-EX| support a |ROSTER|.  Refer to the JMRI documentation or your |WTS-DCC-EX| device's documentation for creating a |ROSTER|.

Filter the Roster
''''''''''''''''''

The 'Roster' can be filtered by entering text in the ``Contains...`` field.

As you type each character the filter will be applied and the list will be reduce to only those entries that contain the text you have entered.

The filter is case insensitive.


Download to the Roster
'''''''''''''''''''''''

By clicking the :guilabel:`Download` button, all locos in the Server roster will be drawn in the 'Recent List' in |ED|.  

For this the filter is ignored. i.e. the Whole Server Roster is downloaded, not just what you can see on screen.

Note that if there are more locos in the Roster than, the :ref:`configuration/preferences:maximum recent locos` preference value, the Maximum Recent Locos will be automatically increased the number in the roster + 1.

Icons / Loco Images
''''''''''''''''''''

**From the Server**

|ED| is designed to retrieve the Loco Images from JMRI if provided.  To do this, JMRI's Web Server must be enabled :menuselection:`DecoderPro --> Actions --> Start Web Server`

The images will be loaded gradually, after |ED| connects to the server and you use the `Loco Select Screen`_ for the first time.

Each time you Acquire a loco, any icon is cached in |ED|, so will load faster that others the next time you use |ED|.

**Adding a local image**

For locos in a Roster from a non-JMRI |SERVER|, that does not support loco icons, you can add a local image as an icon for the entry.

Long Press on a Roster Entry you will see

* A :guilabel:`New Image` button
* The existing image if there is one
* A :guilabel:`Remove` button, if there is an existing image
* A :guilabel:`Save` button

AS long as you have granted the :ref:`about/privacy-policy:optional permissions` you will be able to use the :guilabel:`New Image` button to find and select an image stored on your device/phone to use as a Loco Icon.

.. warning::

  The size of the image must be relatively small. 

  If you select an image but nothing happens, try reducing the size the image, then try again.

Select from Recent Locos List
"""""""""""""""""""""""""""""

Shown if you select ``Recent Locos`` in the `Selection Method`_.

|ed| remembers the last 10 locos that you have selected. (That number can be increased or decreased with :ref:`Maximum Recent Locos <configuration/preferences:maximum recent locos>` preference.)

If the loco you want to control to is in the list, simply click on it and you will be taken back to the |T-S| with that loco selected.

Remove Recent Loco entries
'''''''''''''''''''''''''''

To remove a **single entry** from the recent Locos list, swipe right on that entry.

To remove all entries, click the :guilabel:`CLear List` button.

Naming a Recent Loco
''''''''''''''''''''

For locos that have bee acquired by DCC Address, and are now in the Recent Locos list, these locos can be renamed.

Long Press on the entry in the Recent Locos list, and enter a new name.

Select from Recent Consists (MU) list
""""""""""""""""""""""""""""""""""""""

Shown if you select ``Recent Consists (MU)`` in the `Selection Method`_.

Selecting a |consist| in the Recent Consists (MU) list will automatically add all the remembered locos, including their facing.

Naming a Recent Consist (MU)
''''''''''''''''''''''''''''

For all Recent Consists (MUs) these Consists (MUs) can be renamed.

Long Press on the entry in the Recent Consist (MU) list, and enter a new name.

Remove Recent Consists (MU) Entries
''''''''''''''''''''''''''''''''''''

To remove a **single entry** from the recent Consists (MU) list, swipe right on that entry.

To remove all entries, click the :guilabel:`CLear List` button.


Select Loco - Core On Screen Buttons
"""""""""""""""""""""""""""""""""""""

Acquire
'''''''

  Shown if you select ``DCC Address`` in the `Selection Method`_.

  After you enter a loco's DCC address you press :guilabel:`Acquire` to select the loco.  You will then be taken back to the |T-S| with that loco selected.

Release
'''''''

  Shown if you have one or locos already selected (acquired) for that throttle.

  Clicking this button will release all the locos currently controlled by the throttle.

Edit Order & Facing
'''''''''''''''''''

  Shown if you have one or locos already selected (acquired) for that throttle.

  Clicking this button will show the `<Consist Edit Screen>`_.

Edit Lights
'''''''''''

  Shown if you have one or locos already selected (acquired) for that throttle.

  Clicking this button will show the `<Consist Lights Edit Screen>`_.

Loco Sounds
''''''''''''

  Shown if you have one or locos already selected (acquired) for that throttle.

  Clicking this button will show `<In Phone Loco Sounds Screen>`_.

Consist Edit Screen
^^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/consist_edit2.png
  :align: right
  :scale: 12%


.. todo:: 
  :class: todo-float-right
  
  HIGH: Consist Edit Screen

Shown if you add a second, or subsequent, loco to a throttle via the :guilabel:`Select` button, or if you click on the :guilabel:`Edit Order & Facing` button on the *Select Loco Screen* (which will only be available if you have already acquired more than one loco on the throttle.)

|force-break|

Lead Loco
"""""""""

.. todo:: 
  :class: todo-float-right
  
  HIGH: Lead Loco

|FORCE-BREAK|

Trailing Loco
"""""""""""""

.. todo:: 
  :class: todo-float-right
  
  HIGH: Trailing Loco

|FORCE-BREAK|

Consist Top
"""""""""""

.. todo:: 
  :class: todo-float-right
  
  HIGH: Consist Top

* Change Facing

|FORCE-BREAK|

Consist Lights Edit Screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/consist_lights_edit2.png
  :align: right
  :scale: 12%

.. todo:: 
  :class: todo-float-right
  
  MEDIUM: Consist Lights Edit Screen

* Unknown
* Follow Fn Btn
* Off

|FORCE-BREAK|

Power Screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/power.png
  :align: right
  :scale: 12%

Accessed from any of the main screen via : :menuselection:`Menu --> Preferences --> Left/Right Swipe Preferences --> Power` or from the Action Bar if enabled with the `Layout Power button? preference <./configuration/preferences.html#layout-power-button>`_ : :menuselection:`Menu --> Preferences --> Throttle Screen Action Bar Preferences --> Layout Power button?`.

This screen allows you to toggle the state of track power to your layout.

* When the button is **Green**, it indicates that track power is 'On'.
* When the button is **Red**, it indicates that track power is 'Off'.
* When the button is **Amber**, it indicates that track power state is unknown.
* Pressing a **Green** button will cause the button to be changed to **Red** and the track power will be turned 'Off'.
* Pressing a **Red** button or **Amber** button will cause the button to be changed to **Green** and the track power will be turned 'On'.

Preferences Screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/preferences-1.png
  :align: right
  :scale: 8%

Accessed from any of the main screens via :menuselection:`Menu --> Preferences`.

This screen allows you to personalise  |ed| for how you want it to use it.

.. note:: 
  :class: note-ed-hidden-title

  See the :doc:`Preferences page </configuration/preferences>` for details on the preferences that can be set.

|force-break|

In Phone Loco Sounds Screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/ipls_screen.png
  :align: right
  :scale: 12%

This screen allows you to set |ED| to play synchronised loco sounds through the speaker of your Android device / phone, or through BlueTooth speakers connected to it.

See :ref:`operation/operation:virtual sounds - in phone loco sounds (ipls)` for more information.

Accessed from |T-S| by the :menuselection:`Menu --> Loco Sounds` or from the Status Bar if enabled with the :ref:`In phone sounds button <configuration/preferences:in phone sounds button>` preference.

|force-break|

Function Defaults Screen
^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/function_defaults1.png
  :align: right
  :scale: 8%

This screen allows you to override the appearance of the Function buttons on the throttle screen, primarily for locos that have not been acquired from the |ROSTER|.

.. contents:: The items that can be altered include:
    :depth: 1
    :local:
    :class: in-this-section

Some of these have equivalent items in the preferences.

Accessed from the menu on the |T-S| as :menuselection:`Menu --> Function Defaults`.

Number of Default Functions
""""""""""""""""""""""""""""

This preference is used to limit the number of Function Labels shown for selected locos that are not from the |ROSTER|, or where you have set the :ref:`configuration/preferences:Use default function labels?` preference. 

Number of Default Functions for Roster
""""""""""""""""""""""""""""""""""""""

This preference is used to limit the number of Function Labels shown for |ROSTER| Entries that don't have any function Labels configured.

Use Default Function Labels
""""""""""""""""""""""""""""

If this preference is enabled locos acquired from the |ROSTER| will also use the default function labels as defined on this screen.

Override WiThrottle Default Latching
""""""""""""""""""""""""""""""""""""

If this preference is enabled an additional `Function Latching Settings Screen`_ will be available from the menu.

The DCC-EX Function Settings Screen then allows you override to default latching/momentary behaviour of all/any function for locos acquired from the |EX-CS| by entering is DCC address . i.e. not locos acquired from the roster.

Use Defaults for Roster Entries With no functions
""""""""""""""""""""""""""""""""""""""""""""""""""

If this preference is enabled, locos in the |ROSTER| that have no function buttons defined will show no Function buttons on the Throttle Screen.

If this preference is NOT enabled, locos in the |ROSTER| that have no function buttons defined will show the default functions and and labels as defined on the screen.

This preference is enabled by default.

Function List
""""""""""""""

The function list shows up to 32 functions with both a number and a label.

The **Function Number** defines which DCC function number should be activated when you click the corresponding button on the Throttle Screen.

Not all numbers (0-31) need be included.

The order of the number can be changed.

The **Function Label** defines what label/text should show on the corresponding button on the Throttle Screen.

|force-break|

Function Latching Settings Screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/function_latching_settings.png
  :align: right
  :scale: 8%

.. todo:: 
  :class: todo-float-right
  
  MEDIUM: Function Latching Settings Screen

The function list shows 32 functions with both a label and a drop-list to say if the function should be latching or not (momentary).

This screen is only available in the menu if the `Override WiThrottle Default Latching`_ option is enabled on the `Function Defaults Screen`_ and you are are connected to a WiThrottle server. (Not an |EX-CS| using the DCC-EX Native protocol.)

Accessed from the menu on the |T-S| as :menuselection:`Menu --> Function Latching Settings`.

|force-break|

DCC-EX Function Settings Screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/dcc-ex-functions-screen.png
   :scale: 8 %
   :align: right

This screen allows you to override to default latching/momentary behaviour of all/any function for locos acquired from the |EX-CS| by entering is DCC address . i.e. not locos acquired from the |ROSTER|.

This screen is effectively the same as the `Function Latching Settings Screen`_ but is only available when connected to an |EX-CS| using the DCC-EX Native protocol. (Not WiThrottle protocol)

Accessed from the menu on the |T-S| as :menuselection:`Menu --> DCC-EX Function Settings`.

|force-break|

DCC-EX Screen
^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/dcc-ex-cv-prog-screen.png
   :scale: 8 %
   :align: right

This screen allows you to perform a number of |EX-CS| specific actions including reading and writing CVs.  

See :doc:`/operation/dcc-ex-native-protocol` for more information.

This menu item and screen is only available if connected to a DCC-EX EX-CommandStation using the |NATIVE|.

Accessed from the menu on the |T-S| as :menuselection:`Menu --> DCC-EX`.

|force-break|

WiThrottle - Programming on the Main Screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/pom_screen.png
   :scale: 8 %
   :align: right

This screen allows you to program CVs in decoders on the main (Operation mode programming) on *some* systems / command stations.

Accessed from the menu on the |T-S| as :menuselection:`Menu --> DCC-EX CV Prog on MAIN`.

The menu option is only shown if the :ref:`configuration/preferences:Show WiThrottle PoM Page` preference is enabled.

note: You cannot **READ** CVs.  You can only write them.

.. todo:: 
  :class: todo-float-right
  
  LOW: Programming on the Main Screen

.. warning:: 

  This feature only works on a very small number of Command Stations.  It works by sending a hex packet to the command station.

|force-break|

Gamepad Test Screen
^^^^^^^^^^^^^^^^^^^

.. todo:: 
  :class: todo-float-right
  
  LOW: Gamepad Test Screen

Accessed from the |T-S| via the :menuselection:`Menu --> Gamepads -> Gamepad Test X`. (where 'X' is the number of the gamepad.)

|FORCE-BREAK|

View Log Screen
^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/log_view.png
  :align: right
  :scale: 12%

This screen allows you to view the internal |ED| log of events.
This is sometimes useful for analysing problems.

The option to `Start recording to file` creates a user-accessible file that can be sent to the |ed| app developers or the `Groups.io <https://groups.io/g/jmriusers/topics>`_ help group to assist you in resolving a problem.
The file will be located on your mobile phone at:
Internal storage ``/Android/data/jmri.enginedriver/files``. It will be named something like: ``logcat9999999999999.txt``.

Note: This location cannot be accessed easily on later versions of Android (>13). So to see it or send to the developers for support you must connect your device/phone to a PC.

Enable the :ref:`configuration/preferences:Show Timestamps on Log?` preference to include the timestamp on each line of the log.

Accessed from any of the main screens via :menuselection:`Menu --> View Log`.

|force-break|

About Screen
^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/about.png
  :align: right
  :scale: 12%

This screen displays 

* Information about |ed| 
* Information about the |WTS-DCC-EX| it is currently connected to (if any)
* A page of basic information about |ed|

Displayed information includes:

  * **OS:**  (Android version)
  * **SDK:**
  * **DeviceID:**
  * **IP:** (of the device/phone)
  * **SSID:** 
  * **Net:**
  * **EngineDriver:**  (version)
  * **Protocol:** (WiThrottle or DCC-EX)
  * **Heartbeat:**
  * **Host:** (IP Address)   **Port:**
  * **Server:** (details)

|force-break|

Reconnecting Screen
^^^^^^^^^^^^^^^^^^^

.. todo:: 
  :class: todo-float-right
  
  MEDIUM: Reconnecting Screen
 
This screen displays if |ed| has not been able to communicate with the |WTS-DCC-EX| within a specified time.

Common Elements and Features
----------------------------

This section describes some of the elements and features that appear throughout or affect the entire |ed| app.

* `Theme / Styles`_
* `Localisation`_
* `Action Bar`_
* `Overflow Menu`_ (the Menu)

Theme / Styles
^^^^^^^^^^^^^^

Themes provide different colours and textures to the buttons, backgrounds, sliders etc. for all the screens in |ed|.  i.e. It changes the appearance of the entire app.

There are a number of themes to choose from:

.. list-table::
    :widths: auto
    :header-rows: 1

    * - Example
      - Theme
    * - .. image:: ../_static/images/screenshots/throttle_horizontal_original_theme.png  
          :scale: 8%
      - Original theme
    * - .. image:: ../_static/images/screenshots/throttle_horizontal_high_contrast_theme.png 
          :scale: 8%
      - High contrast theme 
    * - .. image:: ../_static/images/screenshots/throttle_horizontal_outline_theme.png
          :scale: 8%
      - High contrast
    * - .. image:: ../_static/images/screenshots/throttle_horizontal_dark_theme.png
          :scale: 8%
      - Dark theme
    * - .. image:: ../_static/images/screenshots/throttle_horizontal_colorful_theme.png
          :scale: 8%
      - Colourful theme
    * - .. image:: ../_static/images/screenshots/throttle_semi_realistic_neon_blue_theme.png
          :scale: 8%
      - Neon Blue theme

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Theme / Style preference <configuration/preferences:theme/style>` on the preferences page for more information.

Localisation
^^^^^^^^^^^^

Changing the *Localisation* primarily changes the language used in the menus, buttons and messages throughout |ED|.

Supported localisations are:

* Use Phone's global setting
* English (US)  - Engine Driver's default
* English (UK)
* English (AUS)
* English (NZ)
* Italian
* Portuguese
* German
* Spanish
* Catalan
* French (FR)
* French (CA)
* Czech
* Japanese

.. note:: 
   :class: note-ed-hidden-title

   See the :ref:`Localisation preference <configuration/preferences:Localisation>` on the Preferences page for more information.

Action Bar
^^^^^^^^^^

.. image:: ../_static/images/parts/action_bar.png
   :align: right
   :scale: 50%

The Action Bar appears at the top of all screens. It will show different information and different buttons depending on a\) the particular screen and b\) preferences you have set.

The Action Bar can display:

* The app name (|ed|)
* Optionally configured information:

  * Fast Clock
  * Children's Timer Status and Countdown
  * Full Screen or Action Bar Only left/right swipe
  * |WTS-DCC-EX| Name

* Optionally configured buttons:

  * Emergency Stop  (EStop)
  * Track Power
  * Flashlight
  * Throttle Web View
  * Throttle Layout Switching
  * In Phone Loco Sound
  * DCC-EX
  * Children's Timer

The optional buttons are enabled and configured via the corresponding preferences in the :ref:`Throttle Screen Action Bar <configuration/preferences:throttle screen action bar preferences>` preference group.  (Other than the Children's Timer which is configured in the :ref:`Children's Timer <configuration/preferences:children's (timer) preferences>` preference group.)

Emergency Stop Button
"""""""""""""""""""""

.. image:: ../_static/images/parts/estop.png
   :align: right
   :scale: 50%

The *Emergency Stop* Action Bar button is enabled with the :ref:`Emergency Stop button? <configuration/preferences:emergency stop button?>` preference.

Clicking this button will attempt to quickly stop all locos controlled by the device / phone.  Locos controlled by other people/devices are not stopped.

Track Power Button
""""""""""""""""""

.. image:: ../_static/images/parts/power_green.png
   :align: right
   :scale: 50%

The *Track Power* Action Bar button is enabled with the :ref:`Layout Power button? <configuration/preferences:layout power button?>` preference.

*Track Power*, when pressed will turn on/off the power to the track.  The colour of the button will change colour:

* 'Amber' = unknown state
* 'Red' = Power is Off
* 'Green' = Power is On

Flashlight Button
"""""""""""""""""

.. image:: ../_static/images/parts/flashlight_on.png
   :align: right
   :scale: 50%

The *Flashlight* Action Bar button is enabled with the `Flashlight button? <../configuration/preferences.html#flashlight-button>`_ preference.

*Flashlight*, when pressed will turn on/off the Device's camera light.

The device / phone must have a camera to be able to use this feature.

Throttle Web View Button
""""""""""""""""""""""""

.. image:: ../_static/images/parts/web_view.png
   :align: right
   :scale: 50%

The *Throttle Web View* Action Bar button is enabled with the `Throttle Web View button? <../configuration/preferences.html#throttle-web-view-button>`_ preference.

*Throttle Web View*, when pressed will show or hide the :ref:`Throttle Web View <operation/interface:web view area (throttle web view)>` panel on the |T-S|.

Note: the :ref:`Throttle Web View? <configuration/preferences:throttle web view?>` preference must be enabled for this to have an effect.

Layout Switch Button
""""""""""""""""""""

.. image:: ../_static/images/parts/throttle_switch_button.png
   :align: right
   :scale: 50%

The *Layout Switch* button, when pressed will swap the :ref:`Throttle Screen Layout <configuration/preferences:throttle screen layout>` between two predefined layouts.

The *Layout Switch* Action Bar button is enabled with the `Show Layout Switch button <../configuration/preferences.html#show-layout-switch-button>`_ preference.


DCC-EX Button
""""""""""""""""""""""""""

The *DCC-EX* button, when clicked will open the `DCC-EX Screen`_.

The *DCC-EX* Action Bar button is enabled with the :ref:`configuration/preferences:dcc-ex button?` preference and is only available when connected to a |EX-CS| using the |NATIVE|. 

In Phone Loco Sound Button
""""""""""""""""""""""""""

.. image:: ../_static/images/parts/in_device_sounds_outline.png
   :align: right
   :scale: 50%

*In Phone Loco Sounds*, when clicked will open the `In Phone Loco Sounds Screen`_.

The *In Phone Loco Sounds* Action Bar button is enabled with the :ref:`In Phone Loco Sounds Button <configuration/preferences:In Phone Sounds Button>` preferences.

Children's Timer Button
"""""""""""""""""""""""

.. image:: ../_static/images/parts/timer.png
   :align: right
   :scale: 50%

The *Children's Timer Button*, when pressed will activate the Timer for the preset time period.

The *Children's Timer Button* Action Bar button is enabled with the :ref:`configuration/preferences:show timer button?` preference.

.. note:: 
  :class: note-ed-hidden-title

  See the `Children's Timer section <../operation/advanced.html#children-s-timer>`_ of the Advance Operation page for more information.

Fast Clock
""""""""""

.. image:: ../_static/images/parts/fast_clock.png
   :align: right
   :scale: 50%

.. todo:: 
  :class: todo-float-right
  
  LOW: Fast Clock

The *Fast Clock* Action Bar button is enabled with the `Fast Clock Display <../configuration/preferences.html#fast-clock-display>`_ preference.

.. note:: 
  :class: note-ed-hidden-title

  See `JMRI's Fast Clock page <https://www.jmri.org/help/en/package/jmri/jmrit/simpleclock/SimpleClockFrame.shtml>`_ for information on how to set up a Fast Clock.

|BR|

Children's Timer Status and Countdown
"""""""""""""""""""""""""""""""""""""

.. image:: ../_static/images/parts/childrens_timer_countdown.png
   :align: right
   :scale: 50%

.. todo:: 
  :class: todo-float-right
  
  LOW: Children's Timer Status and Countdown

.. note:: 
   :class: note-ed-hidden-title

   See the :ref:`Children's Timer part <operation/advanced:children's timer>` of the Advance Operation page for more information.

|BR|

Full Screen or Action Bar Only left/right swipe
"""""""""""""""""""""""""""""""""""""""""""""""

.. todo:: 
  :class: todo-float-right
  
  LOW: Full Screen or Action Bar Only left/right swipe

|FORCE-BREAK|

WiThrottle Server Name
""""""""""""""""""""""

.. image:: ../_static/images/parts/action_bar_server_name.png
   :align: right
   :scale: 50%

.. todo:: 
  :class: todo-float-right
  
  LOW: WiThrottle Server Name

|FORCE-BREAK|

Overflow Menu
^^^^^^^^^^^^^

.. image:: ../_static/images/parts/menu_throttle.png
  :align: right
  :scale: 50%

The *Overflow Menu* (or simply '*Menu*') appears in the Action Bar at the top of most of the `main screens <../operation/interface.html#main-screens>`_ is normally three dots (⁞) or three bars (≡).
It will show different options depending on a) the particular screen, b) preferences you have set and c) the state of certain elements in the app.

The Overflow Menu can display:

* :ref:`Intro/Setup Wizard <operation/interface:intro/setup wizard screen>`)
* :ref:`Clear Recent List <operation/interface:connection screen>` (|C-S| only)
* :ref:`Throttle <operation/interface:throttle screen>` (All except the |T-S| only)
* `Turnouts/Points Screen`_ (All except the *Turnout/Points Screen* only)
* :ref:`Routes <operation/interface:routes screen>` (All except the |R-S| only)
* :ref:`Power <operation/operation:turn track power on>`
* `DCC-EX Screen`_ (If connected to a DCC-EX EX-CommandStation using the |NATIVE| only)
* :doc:`Preferences </configuration/preferences>`
* :ref:`Function Defaults <operation/interface:Function Defaults Screen>` (|T-S| only)
* Gamepads (|T-S| only)

  * :ref:`Gamepad Test 1 <operation/interface:gamepad test screen>`
  * :ref:`Gamepad Test ... <operation/interface:gamepad test screen>`

* :ref:`Loco Sounds <operation/interface:in phone loco sounds screen>` (|T-S| only)
* :ref:`View Log <operation/interface:view log screen>`
* :ref:`Exit <operation/operation:exiting engine driver>`
* :ref:`About <operation/interface:about screen>`
