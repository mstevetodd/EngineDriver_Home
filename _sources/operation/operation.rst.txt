****************************************************************************
Detailed Instructions |BR| |SMALL-START| Operating Engine Driver |SMALL-END|
****************************************************************************

.. meta::
   :keywords: operation

.. include:: ../include.rst

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
     :local:
     :depth: 2

Connecting
^^^^^^^^^^^^^^^^

Connecting has two aspects:

1. Connecting to the WiFi network, which uses Android's built in capabilities (not |EDs|)
2. Connecting |ED| to the |WTS-DCC-EX|

Connecting to the WiFi network
""""""""""""""""""""""""""""""

  .. image:: ../_static/images/parts/network1.png
    :scale: 40 %
    :align: right

* Use Android's System Network - Wifi settings to connect to the same network as your |WTS-DCC-EX|
* With some exceptions, your device's IP Address should be similar to the server's IP address (the first three blocks of numbers will be identical)

  .. image:: ../_static/images/parts/network2.png
    :scale: 30 %
    :align: right

  * For your Android device / phone, you can see its address in the |EDs| 'About Screen' (:menuselection:`Menu --> About`), at the top of the screen
  * For a |JMRI| server, see the WiThrottle screen for its address 
  * For other devices, see the instructions for that device

.. note:: 
  :class: note-ed-hidden-title
  
  Also see the :doc:`WiFi issues </operation/wifi_issues>` page if you are having difficulties.

Connecting Engine Driver to the |server|
"""""""""""""""""""""""""""""""""""""""""""""""""

* Start |ED| |BR|\ You will be presented with the |C-S|
* On the |C-S| there are three ways you can select a |WTS-DCC-EX| to connect to:

  - `IP Address and Port`_
  - `Discovered Servers List`_ (The most common way to connect)
  - `Recent server List`_

IP Address and Port
'''''''''''''''''''
.. image:: ../_static/images/parts/connecting_ip_address.png
  :scale: 50 %
  :align: right
  :name: IP Address

Type in the **IP address** and **Port** of the |WTS-DCC-EX| and press :guilabel:`Connect`.

To find your server's IP address and Port:

  * For a |JMRI| server, see the WiThrottle screen for its address 
  * For other |SERVERS|, see the instructions for that device

If you only ever connect to one |WTS-DCC-EX| you can effectively bypass this screen by setting the :ref:`Auto-Connect to WiThrottle Server? <configuration/preferences:auto-connect to withrottle server?>` preference.

.. note:: 
  :class: note-ed-hidden-title

  Also see :doc:`Connection issues </operation/wifi_issues>` if you are having difficulties.

Discovered Servers List
'''''''''''''''''''''''

.. image:: ../_static/images/parts/connecting_discovered_servers.png
  :scale: 50 %
  :align: right
  :name: Discovered Servers

**This is the most common way to connect.** If the |SERVER| you want to connect to is in the list, simply click on it and you will be taken to the |T-S|.

If the |SERVER| does not appear in the recent list try one of the other two methods.  
Your |SERVER| not appearing in the recent list is not necessarily a problem  See :doc:`Connection issues </operation/wifi_issues>` for more information.

Recent Server List
''''''''''''''''''

.. image:: ../_static/images/parts/connecting_recent_servers.png
  :scale: 50 %
  :align: right
  :name: Recent Severs

If the |SERVER| you want to connect to is in the list, simply click on it and you will be taken to the |T-S|.

Note: A |SERVER| being in this list *does not* necessarily mean that you will be able to connect it *now*. It just means that you have successfully connected to it in the past.

There is also a 'demo' |WTS| at **jmri.mstevetodd.com**, port **44444** in this list that you can connect to for testing. (If your device/phone has an internet connection.)

Disconnections
""""""""""""""

|ed| and/or the Android device can occasionally lose the connection even after it successfully connected.  There can be a lot of causes.  If ED does lose connection it will buzz, vibrate and take you to *Reconnecting Screen*.   It will repeatedly and indefinitely attempt to reconnect.

If |JMRI| does not receive any feedback from your device/phone within a configured period, |JMRI| will stop all the locos you have selected on you device/phone.

.. note:: 
  :class: note-ed-hidden-title
  
  See :ref:`WiFi issues <operation/wifi_issues:disconnections>` more information for possible causes/solution.

  See :ref:`Feedback on Disconnect preference on the Preferences page <configuration/preferences:feedback on disconnect>` to disable the audible and haptic warnings.

Turn Track Power On
^^^^^^^^^^^^^^^^^^^

Some |CSs| need to be instructed to turn the Track Power on before you can use them.  This is not required by all |CSs| so check your manufacturer's instructions.

There are two ways to turn the Track Power on/off:

* Power Screen - accessed from the menu
* Power Action Bar button - if enabled in the preferences
 
The *Power Screen* can be accessed from the :menuselection:`Menu --> Power`.  This will open the Power Screen where there is a simple button that to turn the power on or off. Use Android's ``Back`` button to return to the Throttle Screen.

If the *Power Action Bar button* is enabled, simply click on it to turn track power on or off.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Power section of the User Interface page <operation/interface:Power Screen>` for more information.
  
  See the :ref:`Power Button option in the Preferences page <configuration/preferences:throttle screen action bar preferences>` for more information on enabling the Power Button on the Action bar.

Selecting & Releasing Locos
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Selecting and releasing locos and |consists| is initiated from the Throttle Screen, by clicking on the :guilabel:`Select` button of one of the Throttles on the screen.

(The |T-S| may have from 1 to 6 throttles on it, depending on the :ref:`Throttle Screen Layout preference <configuration/preferences:throttle screen appearance preferences>` you have chosen.)

Selecting a Single loco
"""""""""""""""""""""""

There three ways select a loco:

* By entering a `DCC Address`_
* By selecting from the `Server Roster`_
* By selecting a `Recent Loco <Recent Locos>`_

DCC Address
'''''''''''

You can enter the loco's DCC address (verify short or long), and press :guilabel:`Acquire` to select the loco.  You will then be taken back to the |T-S| with that loco selected.

Server Roster
''''''''''''''

If the loco you want to control is in the list, simply click on it and you will be taken back to the |T-S| with that loco selected.

For this to be possible, the Loco you want to control needs to be in the |ROSTER| of the |WTS-DCC-EX|.  Not all |WTS-DCC-EX| support a |ROSTER|.  Refer to the JMRI documentation or your |WTS-DCC-EX| device's documentation for creating a roster.

.. Also see `Locomotive Icons <locomotive icons in the roster>`_ below.

Recent Locos
''''''''''''

|ed| remembers the last 10 locos that you have selected. (That number can be increased or decreased with :ref:`Maximum Recent Locos <configuration/preferences:maximum recent locos>` preference.)

If the loco you want to control to is in the list, simply click on it and you will be taken back to the |T-S| with that loco selected.

On the fly / In Phone Consists (Multiple Units)
""""""""""""""""""""""""""""""""""""""""""""""""

There two ways create a |consist| train:

*  **Selecting additional locos, one loco 'at a time' (as above)**

      * `DCC Address`_
      * `Server Roster`_
      * `Recent Locos`_

* By using the **Recent Consists** list 

One at a time
'''''''''''''

Adding additional locos to the |consist| train is identical to the process of selecting a single loco.  Simply click on the :guilabel:`Select` button, which will be showing the name or address of any locos already selected.

After selecting each additional loco, the :ref:`operation/interface:Consist (MU) Edit Screen` will be shown. This allows you to:

* Change the facing of each loco (except the front loco)
* Change the order of the locos in the |consist|
* Remove locos from the |consist|

Recent Consists
'''''''''''''''

Selecting a |consist| in the Recent Consists list will automatically add all the remembered locos, including their facing to the selected locos on the current throttle.

.. note::
  :class: note-ed-hidden-title

  Note:

  * There is no real limit to the number of locos that can be added to a |consist|.
  * The order of the locos in the consist can be important.  By default, lights and sound functions are only sent to the first loco.  This can be overridden in the preferences.

Running Trains
^^^^^^^^^^^^^^^

Once you have selected a |loco_consist| for a throttle, the names or addresses of the locos will be shown in the :guilabel:`Select` button of the throttle.

From here you can:

* Control the speed and direction of you |loco_consist|
* Activate the DCC functions for you |loco_consist|
* Activate the Virtual Sounds 
* Add or release locos.  
  
.. note:: 
  :class: note-ed-hidden-title

  See `Selecting / Releasing Locos and Consists/Multiple Units <selecting releasing locos>`_ for more information.

Controlling Speed
"""""""""""""""""

There are eight ways you can control the speed of of your |loco_consist| train:

* `Sliders`_ (if available in the Throttle layout)
* `Speed buttons`_ (if enabled)
* `Stop button`_
* `Volume keys`_
* `Emergency Stop - Action Bar button`_ (if enabled)
* `Pause button`_ (if enabled)
* `Limit Speed button`_ (if Enabled)
* `Gamepad keys - Speed control`_ (if connected)

Sliders
'''''''

Dragging you finger along the slider will increase or decrease the speed of the loco(s) selected for the that Throttle. Pressing and holding your finger at one spot on the slider will cause |ED| to slowly increase or decrease the speed of the loco(s) selected for the that Throttle till it gets to that point.
  
  Depending on the :ref:`Throttle Screen Layout <configuration/preferences:throttle screen layout>` chosen all sliders on the |T-S| will be either:
  
  * one-directional (0% - 100%) |BR|\ or 
  * bi-directional (-100% - 0 - +100%) 

In most Throttle Screen layouts it is possible hide the Speed Sliders.  

.. note:: 
  :class: note-ed-hidden-title

  See the :doc:`Speed Slider and Buttons section on the Preferences page </configuration/preferences>` for more information.

Speed Buttons
'''''''''''''

The Throttles on the Thro|T-S| may configured have ``++`` and ``--`` *Speed Buttons* that allow you to increase or decrease the loco's speed.  

Click on the ``Forward`` or ``Reverse`` buttons to increase of decrease the speed in by a defined Amount.

Click and Hold on the button continually increase the speed by a defined steps.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Display Speed buttons? <configuration/preferences:display speed buttons?>` preference in the :ref:`Speed Slider and Buttons section on the Preferences page <configuration/preferences:Speed Slider and Buttons Preferences>` for more information on enabling the *Speed Buttons*.

  See the :ref:`Throttle Screen Layout preference on the Preferences page <configuration/preferences:throttle screen layout>` for more information on the Throttle Screen Layouts that support *Speed Buttons*.

  See the :ref:`Speed button Change Amount preference in the Throttle Control Preferences section on the Preferences page <configuration/preferences:speed button change amount>` for more information on changing how much the speed changes on each click.

Stop button
'''''''''''

Click on the :guilabel:`Stop` button of a Throttle on the |T-S| to stop all the select Locos for that Throttle.  If you have momentum configured for in the decoders in the locos, they will gradually come to a stop.

Volume Keys
''''''''''''

The :guilabel:`Volume Up` and :guilabel:`Volume Down` hardware keys of your device / phone act exactly the same at as the Speed Buttons of the 'current' Throttle. 

Click on the :guilabel:`Volume Up` and :guilabel:`Volume Down` buttons to increase of decrease the speed in by a defined Amount.

Click and Hold on the button continually increase the speed by a defined steps.

The *Volume Keys* can only affect one throttle at a time.  Which throttle is being controlled by a small 'V' in the Throttle Speed amount area. To change to another Throttle, click on the Throttle Speed amount area of another Throttle.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Volume Button Preferences section on the Preferences page <configuration/preferences:speed button change amount>` for more information on disabling the Volume Keys and changing how much the speed changes on each click. 

Emergency Stop - Action Bar button
''''''''''''''''''''''''''''''''''

.. image:: ../_static/images/parts/estop.png
  :align: right
  :scale: 50%

If enabled, the :guilabel:`Emergency Stop` button on the Action Bar will attempt to stop all the locos on all the Throttles controlled by your device / phone as quickly as possible.

It *does not* stop locos controlled by other people / controllers.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Emergency Stop button? Preference on the Preferences page <configuration/preferences:emergency stop button?>` for more information on enabling the :guilabel:`Emergency Stop` button. 

Pause button
''''''''''''

.. image:: ../_static/images/parts/pause_button.png
  :align: right
  :scale: 50%

If enabled, the :guilabel:`Pause` button will gradually bring the Loco (or |consists|) on the Throttle to gradually step down to the zero speed.  Clicking the button again will gradually return the Loco (or |consist|) on the Throttle back to the speed that it was before you fist pressed the button.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`'Limit Speed' & 'Pause' button Preferences section on the Preferences page <configuration/preferences:'Limit Speed' & 'Pause' button Preferences>` for more information on enabling the :guilabel:`Pause` button. 

Limit Speed button
''''''''''''''''''

.. image:: ../_static/images/parts/limit_speed_button.png
  :align: right
  :scale: 50%

If enabled, the :guilabel:`Limit Speed` button will restrict the maximum speed on the Throttle to predefined amount. (Default is 50%)  Clicking the button again will take off the restriction. (i.e. back to 100%)

This is commonly used for Switching/Shunting work VS mainline running.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`'Limit Speed' & 'Pause' button Preferences section on the Preferences page <configuration/preferences:'Limit Speed' & 'Pause' button Preferences>` for more information on enabling the :guilabel:`Limit Speed` button. 

Gamepad keys - Speed Control
''''''''''''''''''''''''''''

.. image:: ../_static/images/gamepads/bt_controller2.jpg
  :align: right
  :scale: 20 %

Any keys and/or the any DPad directions can be configured to change Speed, Stop, Emergency Stop, Pause or Limit Speed.

.. note:: 
  :class: note-ed-hidden-title

  See the :doc:`Gamepads Operation page </operation/gamepads>` for information on selecting and using a gamepad.

  See the :doc:`Gamepads Configuration page </configuration/gamepads>` for information on configuring the keys of the gamepad.


Controlling Direction
""""""""""""""""""""""""""

There are three ways you can control the direction of your |loco_consist| train:

* `Direction Buttons`_ - for throttle screen layouts with direction buttons
* `Sliders <Sliders - Switching/Shunting Throttle Screen layouts>`_ - For throttle screen layouts without direction buttons  (Switching/Shunting)
* `Gamepad keys - Direction control`_

Direction Buttons
'''''''''''''''''

.. image:: ../_static/images/parts/direction_buttons.png
  :align: right
  :scale: 50%

Throttles on Throttle Screen Layout that are *not* of the Switching/Shunting type have :guilabel:`Forward` and :guilabel:`Reverse` *Direction Buttons* for each throttle.  

Clicking on a button will change the direction of the loco ( or |consist|) if it is not already moving in that direction. 

The *Direction Buttons* can be:
* Disabled while the loco (or |consist|) is moving. (i.e. the speed in either direction is greater that zero.)
* Re-labelled
* Can be swapped

*Direction Buttons* are Not available on the Switching/Shunting Throttle Screen layouts.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Throttle Screen Layout preference on the Preferences page <configuration/preferences:throttle screen layout>` for more information on the Throttle Screen Layouts that support *Direction Buttons*.

  See the :ref:`Swapping Direction Buttons <operation/advanced:swapping direction buttons>`  or  :ref:`Renaming Direction Buttons <operation/advanced:renaming direction buttons>` On the Advanced Operation page for information on swapping or renaming the buttons.
  
  See the :ref:`Direction Button Preferences section of the Preferences page <configuration/preferences:direction button preferences>` for additional options for configuring the *Direction Buttons*.

Sliders - Switching/Shunting Throttle Screen layouts
''''''''''''''''''''''''''''''''''''''''''''''''''''

.. image:: ../_static/images/parts/slider_vertical_switching.png
  :align: right
  :scale: 40 %

Depending on the  :ref:`Throttle Screen Layout <configuration/preferences:throttle screen layout>` chosen sliders on the |T-S| can be b-directional.  (Switching / Shunting Layouts)

Switching / Shunting Layouts have 'stationary' (zero speed) at the centre of the slider.  Dragging your finger along the slider to the right (or up) from the centre will increase the speed of the loco(s) selected for that Throttle *in the forward direction*. Dragging your finger along the slider to the left (or down) from the centre will increase the speed of the loco(s) selected for the that Throttle *in the reverse direction*. 

Pressing and holding your finger at one spot on the slider will cause |ED| to slowly increase or decrease the speed of the loco(s) selected for the that Throttle till it gets to that point.  If the point you are holding is on the opposite half of the slider the speed will slowly decrease speed to zero, then slowly increase speed in the opposite direction to the point you are holding.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Throttle Screen Layout preference on the Preferences page <configuration/preferences:throttle screen layout>` for more information on the Throttle Screen Layouts that support the Switching / Shunting Layouts.

Gamepad keys - Direction Control
''''''''''''''''''''''''''''''''

.. image:: ../_static/images/gamepads/bt_controller2.jpg
  :align: right
  :scale: 20 %

Any keys and/or the any DPad directions can be configured to change direction directly or indirectly (by changing speed when using a switching / shunting throttle Screen Layout).

.. note:: 
  :class: note-ed-hidden-title

  See the :doc:`Gamepads Operation page </operation/gamepads>` for information on selecting and using a gamepad.

  See the :doc:`Gamepads Configuration page </configuration/gamepads>` for information on configuring the keys of the gamepad.

DCC Functions
"""""""""""""""""

There are two ways you can activate the DCC Functions of the decoder in your |loco_consist| train:

- `Function buttons <Activating DCC Functions via the Function Buttons>`_
- `Gamepads keys <Activating the DCC Function via the Gamepad Keys>`_ (if connected)

The DCC functions can be impacted depending on the settings and preferences you have selected:

* `Function Labels`_
* `Functions in consists`_

Activating DCC Functions via the Function Buttons
'''''''''''''''''''''''''''''''''''''''''''''''''

Most (all bar one) Throttle Layouts show a number of DCC Function Buttons below or beside the Sliders for the individual Throttles on the Screen.  Clicking a button will send that function to the Loco (or lead loco of a |consist|.)  This behaviour can be altered in the preferences.

.. note:: 
  :class: note-ed-hidden-title

  See the :doc:`Functions page </configuration/functions>` for information on changing the Functions and Function Labels.

  See the :ref:`Consist Function Follow Preferences on the Preferences page <configuration/preferences:Consist Function Follow Preferences>` for information on changing the behaviour of the functions in |consists|.

Activating the DCC Function via the Gamepad Keys
''''''''''''''''''''''''''''''''''''''''''''''''

Any keys and/or the any DPad directions can be configured to activate the DCC Functions.

.. note:: 
  :class: note-ed-hidden-title

  See the :doc:`Gamepads Operation page </operation/gamepads>` for information on selecting and using a gamepad.

  See the :doc:`Gamepads Configuration page </configuration/gamepads>` for information on configuring the keys of the gamepad.

Function Labels
'''''''''''''''

Most (all bar one) Throttle Layouts show a number of DCC Function Buttons below or beside the Sliders for the individual Throttles on the Screen.

By default:

* If you select a loco from a WiThrottle |ROSTER| Entry, it will show the labels on the buttons as they have been configured in the |ROSTER| Entry on the server. 
* If you enter the DCC address of the loco, it will show |eds| 'Default Function Labels'.  

  * All 29 functions will be shown.  They are: 

    * F0 / Light
    * F1 / Bell
    * F2 / Horn / Whistle
    * F3 - F28

  * Which function buttons, how many function buttons and what labels are displayed, can be changed via the :menuselection:`Menu --> Function Defaults` from the |T-S|

* If you select a Loco from the Recent Locos or Recent Consists lists that was originally selected from a |ROSTER|, |ed| will attempt to show the Labels from the |WTS-DCC-EX| |ROSTER| entry.

.. note:: 
  :class: note-ed-hidden-title

  See the :doc:`Functions page </configuration/functions>` for information on changing the Functions and Function Labels.

|HR-DASHED|

Functions in consists
''''''''''''''''''''''

By default DCC Functions are only sent to the first loco in a |consist|.  This can be changed in the Preferences.

There are a number of preferences that can be used to override the default behaviour.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Consist Function Follow Preferences on the Preferences page <configuration/preferences:Consist Function Follow Preferences>` and the :doc:`Consist Follow Functions page </operation/consist-follow-functions>` for more details.


Virtual Sounds - In Phone Loco Sounds (IPLS)
""""""""""""""""""""""""""""""""""""""""""""

.. important::
  :class: important-float-right

  The IPLS feature of |ED| uses the Notification features of Android, not the Media Player features.

  That means that, at the Android system level, the volume is controlled by the 'Ring and Notification volume' not the 'Media volume'.

|ed| can play synchronised loco sounds through the speaker of your Android device / phone, or through BlueTooth speakers connected to it.

There is built in Support for a number of different type of locos:

* Steam - 4 in-built profiles
* Diesel - 3 in-built profiles
* Plus you can create you own Custom profiles

To enable In Phone Loco Sounds (IPLS) for a throttle (only the first two throttles on an given throttle screen) select an option in :ref:`Throttle 1 Loco Sounds <configuration/preferences:throttle 1 loco sounds>` or :ref:`Throttle 2 Loco Sounds <configuration/preferences:throttle 2 loco sounds>` (or both) preferences. Once enabled for either throttle a new menu option will be available from |T-S| to make subsequent changes easier: :menuselection:`Menu --> Loco Sounds`

To make it easy to switch sound profiles we recommend enabling the Action Bar button by setting the :ref:`In phone sounds button <configuration/preferences:in phone sounds button>` preferences: :menuselection:`Menu --> Preferences --> Throttle Screen Action Bar Preferences --> In phone sounds button`

Automatic Loco Speed Step Sounds
''''''''''''''''''''''''''''''''

Each IPLS Profile has a different number of speed steps. As the loco speed increases or decreases to a certain point a different sound will repeatedly play.  To try to emulate the momentum of the loco, there is a preset delay, and an option to not clip the sounds (which enforces a minimum delay) These can be altered with the :ref:`In Phone Momentum <configuration/preferences:in phone momentum>` and the :ref:`Don't clip loco step sounds <configuration/preferences:don't clip loco step sounds>` preferences.

The volume of the Loco Sounds, the Bell Sounds and the Horn/Whistle sound can be altered independently with the :ref:`In Phone Loco Sounds Volume <configuration/preferences:in phone loco sounds volume>`, the :ref:`In Phone Bell Sounds Volume <configuration/preferences:in phone bell sounds volume>` and the :ref:`In Phone Horn/Whistle Sounds Volume <configuration/preferences:in phone horn/whistle sounds volume>` preferences.

**Playing sounds**

Other than the speed steps sounds, which are automatic, there are three ways to play the additional sounds:

* IPLS specific buttons
* Via the DCC F0, F1, F2 DCC Functions (if set in the preferences)
* Gamepad keys (if connected)

.. note:: 
  :class: note-ed-hidden-title

  See `In Phone Loco Sounds (IPLS) <../configuration/ipls.html>`_ for more information.

**Activating the IPLS Sounds via IPLS Buttons**

Once an IPLS profile is selected for a throttle (either of the first two throttles), four new buttons will be shown near the DCC Function Buttons, with a 'headphones' symbol to distinguish them from the normal DCC Functions.

* Mute (IPLS)
* Bell (IPLS)
* Horn/Whistle (IPLS)
* Short Horn/Whistle (IPLS)

  **Mute button**

  Clicking this will disable all IPLS sounds for this Throttle.

  **Bell button** 

  Clicking this will continuously play a bell sound until it is clicked again (latched)

  The Bell can be made non-latching by changing the :ref:`Bell button Latching/Momentary <configuration/preferences:bell button latching/momentary>` preference.

  **Horn / Whistle button**

  Clicking this will continuously play a horn or whistle sound (depending on the profile) until the button is released (non-latched)

  **Short Horn / Whistle button**

  Clicking this will play a horn or whistle sound (depending on the profile) ones, regardless of how long the button is held down.

  **Activating the IPLS Sounds via DCC Functions / Function Buttons**

  The Bell and Horn/Whistle (long) can be activated by the DCC Function buttons (F1 and F2) if the :ref:`F1 and F2 activate Bell and Horn? <configuration/preferences:f1 and f2 activate bell and horn?>` preference is set.

  **Activating the IPLS Sounds via Gamepad keys**

  Any keys and/or the any DPad directions can be configured to activate/play the IPLS sounds.

  .. note:: 
    :class: note-ed-hidden-title

    See the :doc:`Gamepads Operation page </operation/gamepads>` for information on selecting and using a gamepad.

    See the :doc:`Gamepads Configuration page </configuration/gamepads>` for information on configuring the keys of the gamepad.

Action Bar and Menu
"""""""""""""""""""

Action Bar
''''''''''

.. image:: ../_static/images/parts/action_bar.png
  :align: right
  :scale: 50%

The Action Bar appears at the top of all screens. It will show different information and different buttons depending on the preferences you have set.

The *Action Bar* provides for a number of common and specific information and functions. It can display:

* The app name (Engine Driver)

Optionally configured information:

* Fast Clock
* Children's Timer Status and Countdown
* Full Screen or Action Bar Only left/right swipe
* |WTS-DCC-EX| Name

Optionally configured buttons:

* Emergency Stop (EStop)
* :ref:`Track Power <operation/interface:action bar>`
* Flashlight
* Throttle Web View
* Throttle Layout Switching
* :ref:`In Phone Loco Sounds <operation/interface:action bar>`
* Children's Timer

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Action Bar section of the User Interface page <operation/interface:action bar>` for more information.

Overflow Menu (Throttle Screen)
'''''''''''''''''''''''''''''''
 
The *Overflow Menu* (or simply '*Menu*') appears in the Action Bar at the top of most of the main screens is normally three dots (⁞) or three bars (≡).
It will show different options depending on a) the particular screen, b) preferences you have set and c) the state of certain elements in the app.

These menu items only appear on the |T-S|:

* Function Defaults
* Gamepads

  * Gamepad Test 1
  * Gamepad Test ...

* Loco Sounds

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Overflow Menu section of the User Interface page <operation/interface:overflow menu>` for more information.

Turnouts / Points
^^^^^^^^^^^^^^^^^

|ed| can control DCC controlled Turnouts / Points on your layout if configured in you |WTS-DCC-EX|.

To get the *Turnouts / Points* screen you can use the menu :menuselection:`Menu --> Turnouts/Points` from the main screens.  You can also swipe right from the |T-S| (if enabled in the preference).

The |WTS-DCC-EX| must have Turnouts / Points enabled.

If you've defined your turnouts / points and routes in a panel file, make sure to specify "user names" for those you'd like to see listed on your throttle. You can also "filter" the turnouts shown using the WiThrottle->Filter Controls option in the WiThrottle window.

*Turnouts/Points* can be operated three ways:

* By entering their `DCC Address <By Entering an Address>`_
* From the `Defined Turnout/Point list <Server Defined Turnout/Point list>`_ provided by the |WTS-DCC-EX| (JMRI)
* From the `Recent Turnout/Point list <Recent Turnout/Point list>`_

The |TP-S| can be accessed two ways:

* Menu
* Swipe Left/Right (if enabled)

DCC Address (Turnout/Point)
"""""""""""""""""""""""""""

Enter the DCC address of the Turnout / Points you wish to control.

Enter the address of the Turnout/Point and press any of the buttons:

* :guilabel:`Throw`
* :guilabel:`Close`
* :guilabel:`Toggle`

Server Defined Turnout/Point list
"""""""""""""""""""""""""""""""""

By selecting the 'JMRI Defined' radio button, |ED| will show the Turnouts/Points defined in the |SERVER|.

Click on the button(s) on the beside the entry to :guilabel:`Throw`` or :guilabel:`Close` the Turnout/Point.

Note:

* If the Turnout/Point button says 'Thrown', then clicking on the button will **'Close'** the Turnout/Point and the button will then say 'Closed'.
* If the Turnout/Point button says 'Closed', then clicking on the button will **'Throw'** the Turnout/Point and the button will then say 'Thrown'.

.. note:: 
  :class: note-ed-hidden-title

  Note that this list can optionally be set to *always* show :guilabel:`Close` and :guilabel:`Throw` rather than :guilabel:`Closed` or :guilabel:`Thrown` by setting the :ref:`configuration/preferences:Always Show Throw/Close?` preference.

Filter by location (Turnouts/Points)
""""""""""""""""""""""""""""""""""""

The 'Turnout/Points List' and the 'Routes List' can be filtered.  The filtering relies on the idea that the first part of every Turnout/Point name and ever Route name is a 'Location', followed by a common separator, then the actual name for the Turnout/Point or Route name.  The 'filter' then allows you to select one of those locations and |ed| can just show the Turnout/Points or Routes at the 'Location'.

The :ref:`Location Delimiter <configuration/preferences:location delimiter>` preference allows you to set the character that marks the end of the Location portion of Turnout/Point and Route names.  By default it is a colon (":") but any character can be used.

Recent Turnout/Point list
"""""""""""""""""""""""""

|ed| remembers the last 10 Turnouts/Points that you have controlled.

If the Turnouts/Points you want to control to is in the list, simply click on buttons next to the entry to control it.

|FORCE-BREAK|

Turnout/Point Preferences
""""""""""""""""""""""""""

  See the :ref:`Left/Right Swipe preferences on the Preferences page <configuration/preferences:left/right swipe preferences>` for information on enabling or disabling the swipe though Turnouts/Points.

Overflow Menu (Turnouts/Points Screen)
""""""""""""""""""""""""""""""""""""""

To get the |WV-S| you can use the menu :menuselection:`Menu --> Web` from the main screens.  

The *Overflow Menu* (or simply '*Menu*') appears in the Action Bar at the top of most of the main screens is normally three dots (⁞) or three bars (≡).
It will show different options depending on a) the particular screen, b) preferences you have set and c) the state of certain elements in the app.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Overflow Menu section of the User Interface page <operation/interface:overflow menu>` for more information.

Routes
^^^^^^

|ed| can control *Routes* on your layout if configured in you |WTS-DCC-EX|.

When using |EX-CS| as your |WTS-DCC-EX|, *Routes* can also be used to activate `EXRAIL Automations and Anomations <https://dcc-ex.com/exrail/index.html>`_.

To get the *Turnouts / Points* screen you can use the menu :menuselection:`Menu --> Routes` from the main screens.  You can also swipe left from the |T-S| (if enabled in the preference).

If you've defined your turnouts and routes in a panel file, make sure to specify "user names" for those you'd like to see listed on your throttle. You can also "filter" the turnouts shown using the WiThrottle->Filter Controls option in the WiThrottle window.

The |R-S| can be accessed two ways:

* Menu
* Swipe Left/Right (if enabled)

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Left/Right Swipe preferences on the Preferences page <configuration/preferences:left/right swipe preferences>` for information on enabling or disabling the swipe though Routes.

  See the `Automation (EX-RAIL) page on the DCC-EX website <https://dcc-ex.com/automation/index.html>`_ for more information on using Automations in DCC-EX EX-CommandStations.

By System name
""""""""""""""

You can enter the route ID and click :guilabel:`Set` button to activate a route.

From the Server
"""""""""""""""

You can select the route from the list provider by your |SERVER|...

Click on the :guilabel:`Set` button beside the entry to activate the Route.

Note, When using the |native| the |EX-CS| (only) can:

* Dynamically change the label on the the button
* Dynamically show or hide Routes
* Dynamically enable or disable Routes

Filter by location (Routes)
""""""""""""""""""""""""""""

The 'Turnout/Points List' and the 'Routes List' can be filtered.  The filtering relies on the idea that the first part of every Turnout/Point name and ever Route name is a 'Location', followed by a common separator, then the actual name for the Turnout/Point or Route name.  The 'filter' then allows you to select one of those locations and |ed| can just show the Turnout/Points or Routes at the 'Location'.

The :ref:`Location Delimiter <configuration/preferences:location delimiter>` preference allows you to set the character that marks the end of the Location portion of Turnout/Point and Route names.  By default it is a colon (":") but any character can be used.

Route Preferences
"""""""""""""""""

.. note:: 
  :class: note-ed-hidden-title

  A number of preferences can alter the way Routes are displayed. See :ref:`configuration/preferences:Turnouts/Points and Routes Preferences` for more information.


Overflow Menu (Routes Screen)
"""""""""""""""""""""""""""""""

To get the |WV-S| you can use the menu :menuselection:`Menu --> Web` from the main screens.  

The *Overflow Menu* (or simply '*Menu*') appears in the Action Bar at the top of most of the main screens is normally three dots (⁞) or three bars (≡).
It will show different options depending on a) the particular screen, b) preferences you have set and c) the state of certain elements in the app.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Overflow Menu section of the User Interface page <operation/interface:overflow menu>` for more information.

Panels and Web Pages
^^^^^^^^^^^^^^^^^^^^^^

.. image:: ../_static/images/screenshots/web_view_screen.png
  :align: right
  :scale: 12%

|ed| can show any web page via an embedded Web Browser.  You can use the Web Browser to show anything that JMRI can present including:

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


Throttle Web View VS Web View Screen
""""""""""""""""""""""""""""""""""""

|ed| has two distinct ways you can view web pages.

* Throttle Web View 
* Web View Screen

This section describes the |WV-S|, which is a full screen web browser.  The *Throttle Web View* is a half Screen web browser that optionally shares the screen with the |T-S|. See the :ref:`Throttle Web View section on the User Interface page <operation/interface:Web View Area (Throttle Web View)>` from more information on the Throttle Web View.

The |WV-S| can be accessed three ways:

* `Menu <Overflow Menu (Web View Screen)>`_
* `Swipe Left/Right <Swipe (Web View Screen)>`_ (if enabled)
* `Auto Web Orientation`_

Overflow Menu (Web View Screen)
"""""""""""""""""""""""""""""""

To get the |WV-S| you can use the menu :menuselection:`Menu --> Web` from the main screens.  

The *Overflow Menu* (or simply '*Menu*') appears in the Action Bar at the top of most of the main screens is normally three dots (⁞) or three bars (≡).
It will show different options depending on a) the particular screen, b) preferences you have set and c) the state of certain elements in the app.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Overflow Menu section of the User Interface page <operation/interface:overflow menu>` for more information.

Swipe (Web View Screen)
"""""""""""""""""""""""

You can swipe left or right twice from the |T-S| (if enabled in the preference).
You can also swipe left from the |TP-S| (if enabled in the preference).
You can also swipe right from the |R-S| (if enabled in the preference).

Note that 'Swipe Through Web' is automatically disabled if ``Auto-Web`` orientation is enabled in the :ref:`Screen Orientation <configuration/preferences:screen orientation>` preference.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Left/Right Swipe preferences on the Preferences page <configuration/preferences:left/right swipe preferences>` for information on enabling or disabling the 'swipe though Web', 'Swipe through Routes' and 'Swipe through Turnouts/Points'.

  See the :ref:`Screen Orientation <configuration/preferences:screen orientation>` preference for more information on ``Auto-Web`` orientation option.

Auto Web Orientation
""""""""""""""""""""

If ``Auto-Web`` orientation is selected in the :ref:`Screen Orientation <configuration/preferences:screen orientation>` preference, when you rotate you Android device/Phone from portrait to landscape, the |WV-S| is automatically shown.  Rotating it back will automatically show the |T-S|. 

Note that :ref:`Swipe Through Web <configuration/preferences:swipe through web?>` preference is automatically disabled if ``Auto-Web`` orientation is selelected in the :ref:`Screen Orientation <configuration/preferences:screen orientation>` preference.  It is not automatically re-enabled if you later select a different orientation.  i.e. you will need to manually turn the preference back on if you change from ``Auto-Web`` to another orientation.

.. note:: 
  :class: note-ed-hidden-title

  See the :ref:`Screen Orientation <configuration/preferences:screen orientation>` preference for more information on ``Auto-Web`` orientation option.

  See the :ref:`Left/Right Swipe preferences on the Preferences page <configuration/preferences:left/right swipe preferences>` for information on enabling or disabling the 'swipe though Web', 'Swipe through Routes' and 'Swipe through Turnouts/Points'.


Pushing the app to the Background
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. warning:: 

  |ed| *is not designed to run in background and its performance and continued operation is not reliable or predictable.*

  You should not lock the screen of your Android device/phone while using |ED| for the same reason.

.. image:: ../_static/images/parts/ed_in_background.png
  :align: right
  :scale: 8%

By using the Android :guilabel:`Home` ( ○ ) or :guilabel:`Recent Apps` ( □ ) navigation buttons, or if you press the ``Power`` physical button, it is possible to push the |ed| app into the background.  |ed| will give a sound, warning and will add an entry to the Notification Shade when this happens.

.. image:: ../_static/images/parts/ed_in_shade.png
  :align: right
  :scale: 8%

Clicking on the Notification Shade entry or the app icon will return you to the same screen your were in when you pushed the app to the background.

While |ed| will attempt to continue to run in background, it is at the mercy of the Android OS. Android itself is designed to kill dormant apps, which it will consider this to be, if it thinks there is a better use of the memory or processor, so it can be terminated at any time without warning.

In general avoid letting |ED| try to run in background.

.. note:: 
  :class: note-ed-hidden-title

  If you are concerned about preserving the battery, there are options.  See the :doc:`Conserving Power <../configuration/conserving_power>` page for more information.

  See the :ref:`Background Alert in the Preference page <configuration/preferences:background alert>` for information on disabling the alert.

DCC-EX - Features when using the Native DCC-EX Protocol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Refer to :doc:`this page </operation/dcc-ex-native-protocol>` for details on how to use the |ED| features that are only available when using the **Native DCC-EX Protocol** when connecting to a **EX-CommandStation**.

Exiting Engine Driver
^^^^^^^^^^^^^^^^^^^^^^

You can exit |ED| two ways:

* The Menu
* The Android Navigation :guilabel:`Back` button

**Back button**

* Press the Android :guilabel:`Back` button once from the main screens (more than once if you are on one of the secondary screens). You will be asked if you want to exit. 

|ed| can optionally be configured to exit when the Android :guilabel:`Back` button is pressed twice quickly from the |T-S|.

  See the :ref:`Double Back Buton to Exit? in the Preference page <configuration/preferences:Device Preferences>` for information.

**Menu**

You can select :menuselection:`Menu --> Exit`. You will then be asked if you want to exit. 

|HR-DASHED|

Exiting |ed|:

* Disconnects from the |WTS-DCC-EX|.
* Stops playing all In Phone Loco Sounds (if any were configured).
* It does not necessarily stop any locos that you were controlling.

.. warning::

  A common question is.. *"I have exited Engine Driver, so why is it still showing in the 'Running Apps' list."*

  This is a common misunderstanding.  
  
  The list of apps that shows when you click on the :guilabel:`Recent Apps` ( □ ) navigation button, the square button on the Android Navigation Bar, is **NOT** a list of **Running Apps**.  It is a list of **Recently Used Apps**.

  Android deliberately maintains fragments of every app that runs to make it faster to restart the apps if required.  Android will really kill the app from memory if some other app needs the memory.

  When you see |ED| in this list it is not 'running' *unless* you also see the small |ED| icon on the Android Status Bar at the top of the screen.  If the icon is there, then |ED| is still running.  Instead of exiting, it was pushed to background, where it will attempt to keep running.  As |ED| was not designed to run in background, Android may arbitrarily kill it at any time.