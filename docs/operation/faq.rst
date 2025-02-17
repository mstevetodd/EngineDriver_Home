*******************************************
Frequently Asked Questions
*******************************************
 
.. meta::
   :keywords: FAQ frequently asked questions

.. include:: ../include.rst

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
      :local:
      :depth: 3
    
Connecting - Wifi and WiThrottle
--------------------------------

Q. Why doesn't my Android device automatically connect to my WiFi network?

  A. I have noticed that some older android phones won't automatically reconnect to a network that does not have internet access, and nothing I have been able to do can resolve it.

I have in the past put a shortcut on the homepage to the network settings to make it easy to get there and select the network, before starting ED.

|HR-DASHED|

Q. I can't connect to my Server /Railroad

  A1. Check the following:

  * Check that your device/phone is connected to a WiFi network
  * Check that your device/phone is connected to the same WiFi network as your |WTS-DCC-EX|
  * If using |JMRI|, check that |JMRI| and its |WTS| feature are started

  A2. Possible Mobile data connection problem

  If |ed| can see the |WTS-DCC-EX| but displays an error when you try to connect to it… If you are using a phone with a SIM, and the WiFi network your JMRI server is on does not have internet access. You may have to turn 'mobile data' off on your device.  See `[here] for more information <./wifi_issues.html>`_.

|HR-DASHED|

Q. |ed| Connects, but I can't control any locos

  A. Powering the layout on

  Some |CSs| need you to turn the track power on before you can use it.

  .. note:: 
    :class: note-ed-hidden-title

    See the `Turn Track Power On <../operation/operation.html#turn-track-power-on>`_ notes for more information.

|HR-DASHED|

Q. Why doesn't |ed| automatically find my |WTS-DCC-EX|?

  I can manually connect to my Server / Railroad by entering an IP address, but it never finds it automatically.

  A1. Make sure that the Android System 'Use Location' is enabled.  This must be enabled for |ED| to 'find' servers on the network.

  A2. 4.5ghz and 5ghz.   Some routers do not transfer the mDNS messages between clients on the 4.5ghz and 5ghz channels.  So if your |SERVER| is using 4.5ghz, make sure you device/phone is using a 4.5ghz channel as well. (Or both use 5ghz channels.)

  A3. Mesh Routers.  Many Mesh routers will not transfer the mDNS messages to other connected routers / modems. If you are using a mesh network, make sure both the |SERVER| and the device/phone are using the same Mesh network.

  A4. One reason can be your router doesn't not support the Bonjour/mDNS protocol. There is not much you can do if this is the case other than trying a different router.


|HR-DASHED|

Q. If |ed| can't find my Server/Railroad automatically 

  A. Look for the IP address and port in the WiThrottle window in JMRI 

  Type them in the two fields and click :guilabel:`Connect`

|HR-DASHED|

Q. Why doesn't |ed| remember the servers I have connected to?

  A. Check the |ed| preferences and make sure the ``Maximum Recent Locos`` preference is not set to zero.

----

Connecting to different servers/railroads
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Q. I want to switch to a different server on the same network. 

  A. You need to exit |ed| and restart.

|HR-DASHED|

Q. I want to switch to a different server on a different network. 

  A. You need to exit |ed|, change WiFi networks in the Android settings, then restart |ed|.

----

Save/load preferences for different servers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can set up different preferences for different server/railroads and have them automatically load when you connect to that |WTS-DCC-EX|.
The most common use of this (so far) is to remember the locos relevant to that railroad.  e.g. I run N scale and HO Scale.  When I connect to one of the N Scale layouts I use it shows me my N Scale locos in the recent locos list, but when I connect to one of the HO layouts I use, it shows me the my recently used HO locos.

.. note:: 
  :class: note-ed-hidden-title

  See the `Auto Host Specific Import/Export <../configuration/preferences.html#auto-host-specific-import-export>`_ preference for more information.

|HR-DASHED|

Q. What is this **jmri.mstevetodd.com** in the server list?

  A. *jmri.mstevetodd.com* is a demo server, which can be used for testing. It has |ROSTER| entries, turnouts, routes and an active panel for you to try.

  .. note:: 
    :class: note-ed-hidden-title

    You can use the `Hide Demo Server? <../configuration/preferences.html#hide-demo-server>`_ preference to permanently remove it from the list if you wish.

|HR-DASHED|

Q. How do I clear unwanted servers from the list

  A. Swipe right on an entry to remove it.

Selecting locomotives to control
--------------------------------

Q. Why can't I can't see my loco in the |ROSTER|?

  A. The loco needs to be added to the |ROSTER| on your server computer.  Refer to your server documentation for specifics.

|HR-DASHED|

Q. Why is my loco is not remembered in the recent locos list?

  A1. If the loco is in your |ROSTER|, check the preference ``Roster in Recent Locos?`` so that locos in the |ROSTER| will be included in the recent locos list.

  A2. If no locos are remembered (and you have confirmed the preference above) make sure the ``Maximum Recent Locos`` preference is not set to zero.

|HR-DASHED|

Q. The loco list is too long, I can't find my locos easily

  A. You can use the filter option to reduce the list 

 .. todo:: 
  :class: todo-float-right
  
  LOW: FAQ Selecting locomotives to control

|HR-DASHED|

Q. How do I work with |Consists| / Multiple Units|

  A1. On the fly |Consists| in |ed| 

  |ed| can create |consists| on-the-fly by simply selecting multiple locos, one after the other...

  Note: Make sure that the ``Drop Loco before acquire?`` preference is set to 'No'.

  A2. DCC 'Advanced Consists' (CV19)
 
  Note you can't create a DCC 'Advanced Consists' (CV19) with |ed|, but you can control one if it has already been setup.

  .. todo:: 
    :class: todo-float-right
    
    LOW: FAQ DCC 'Advanced Consists' (CV19)

  Remember that this type of |consist| can cause problems later if the loco has not been removed from the consist first and you want to control it as an individual loco. 

  A3. JMRI Consists

  .. todo:: 
    :class: todo-float-right
    
    LOW: FAQ JMRI Consists

  Creating |consists| in JMRI effectively create DCC 'Advanced Consists' (CV19) and appear in the loco list in |ed| much like any other loco. 

|HR-DASHED|

Q. I can't create on-the-fly |consists| ?

  A. Make sure that the ``Drop Loco before acquire?`` preference is set to 'No'.

|HR-DASHED|

Q. The lights of the locos in my consist are wrong?

  A1. If you use on-the-fly |consists|, you can control the lights by clicking ``Select`` then click on the ``Edit Lights`` button

  A2. You can control the lights with a Long click on the ``Select`` Loco button, if you set the ``Control consist Lights on long click`` preference.

|HR-DASHED|

Q. Can't control my loco?

  A. If you can control the lights but not the motor, check that the loco is not in a 'normal' or 'advanced' consist.

|HR-DASHED|

Q. I sometimes accidently press the volume keys

  A. You can disable the volume keys with the :ref:`configuration/preferences:disable volume keys?` preference.

|HR-DASHED|

Q. I sometimes accidently press the direction button when changing speed

  A. You can:

    * Disable the :ref:`configuration/preferences:Direction change while moving?` preference *(recommended)*
    * :ref:`configuration/preferences:Increase Slider/Speed Height?`
    * :ref:`configuration/preferences:Decrease Loco No. height?`

|HR-DASHED|

Q. No Locomotive Icons appear in the |ROSTER|

  A. The |ROSTER| List, and Recent Locos List on the Select Loco screen will automatically show icons for your locos only if:

    * The **Web Server** (not just the |WTS|) is running on the JMRI server
    * The loco itself has an icon added for it in the JMRI |ROSTER| |BR|\ OR
    * A locally cached or manually chosen image is available for the loco (see 'Locomotive Icons' on the `Operation screen <../operations/index.html>`_)

  Note the |EX-CS| and all other known Commands stations cannot provide |ROSTER| icons.  Only JMRI is know to be able to provide this service.

|HR-DASHED|

Q. Why can't I control 6 locos

  A. only the 'Simple', 'Tablet Switching/Shunting' and 'Tablet Vertical' :ref:`throttle layouts <configuration/preferences:throttle Screen layout>` allows for (up to) 6 throttles.
  
  Also, once you have selected a :ref:`throttle layouts <configuration/preferences:throttle Screen layout>` allows for more throttles, you must also increase the number of throttles displayed with the :ref:`throttle layouts <configuration/preferences:Number of throttles>` preference.

Changing the appearance of Engine Driver
----------------------------------------

Global changes (Themes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Q. I want to change the appearance of the app

  A. You can switch between different themes by changing the preference. 

    * The 'Original' (Checker Plate) theme 
    * The 'High Contrast' Theme. Similar to the original theme, without the textured background with deeper blacks and brighter whites. 
    * The 'High Contrast Outline' theme. For people who like white text on a black background.
    * The 'Dark' theme. 
    * The 'Colourful' theme.
    * the 'Neon Blue' theme

Changing the Throttle screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Q. I want to change the appearance of |T-S|

  A. There are a number of different |T-S| designs/layouts.  Look at the `Operation <../operaion/index.html>`_ screen for details.

    * Default / Original /Horizontal
    * Simple  
    * Vertical
    * Vertical Left
    * Vertical Right
    * Big Buttons - Left
    * Horizontal Switching/Shunting
    * Vertical Switching/Shunting
    * Vertical Switching/Shunting Left
    * Vertical Switching/Shunting Right 
    * Tablet Switching/Shunting Left 
    * Tablet Switching/Shunting Right 
    * Semi-Realistic Left

    |ed| will automatically reload the throttle sceen after closing the preferences screen. 

|HR-DASHED|

Q. I want vertical sliders, not horizontal

  A. See the 'Simple', 'Vertical' and 'Tablet' throttle screen type options above.

|HR-DASHED|

Q. I want to control more than one train 

  A. You can control between one and six trains with |ed|, depending on which |T-S| type (see above) you have chosen. Each train can have one or more locomotives in |consist|. 

     The screen space is shared between throttles, so set the 'Number of Throttles' appropriately.

     Note that the different Throttle Screen options (above) support different numbers on throttles.

|HR-DASHED|

Q. In want to change the labels of the function buttons that are displayed 

  A1. Change the function button defaults in |ed|, for locos without |ROSTER| Entries

  A2. |ROSTER| entries include function button labels, and can be changed when defined to the server

|HR-DASHED|

Q. My locos have different functions but all the Function buttons appear the same for every locomotive 

  A1. There is a Preference “Use default function labels?” which can override the labels from the |ROSTER| entry.  Confirm that you have not turned it on.

  A2. You need to setup the individual functions for each of your locos in JMRI.

|HR-DASHED|

Q. My loco shows the wrong Function labels 

  A. Functions of loco are generally set in the |ROSTER|.  |ed| may be showing the functions of a loco with the same address from the |ROSTER|.

      This can happen if you entered an address to select the loco rather than selecting from the |ROSTER| list.

      You can force the default function labels in the preferences.

Speed slider VS speed buttons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some people find the speed slider difficult to control.

  There are options to:

  * Change the height of slider
  * Add speed buttons to the ends of the slider (with further options to increase the separation)
  * Replace the slider with large speed buttons only.

      (If you are using a gamepad or ESU MCII, then you may like to remove the slider AND the speed buttons.)

|HR-DASHED|

Q. I have a small screen Android device.  It doesn't fit well?

  A1. Try the 'Immersive mode' (Full Screen) preference. (see below)

  A2. Reduce the height of the loco select and direction buttons

  A3. Keep the number of locos to 1 or two.

Direction Buttons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Q. I don't like the direction buttons in that order

  A. If you tend to think that forward should be to the right and reverse to the left, you can change the buttons positions in the preferences.

  You can also change them on the fly.

  Labelling the direction buttons for the directions/conventions of your railroad/railway.

  e.g. North South, West East, Up Down.

  <stuff goes here>


Hiding the title bar and navigation bar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Refer to `Immersive mode (Full Screen)`.

Immersive mode (Full Screen)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:ref:`Immersive mode <configuration/preferences:swipe down action in the throttle view?>` hides the system navigation buttons at the bottom of the screen on the Throttle screen only, to give you more screen real estate for the throttle UI.

It can optionally also hide the Android System Status Bar at the top of the page.

Swiping up from off screen will normally temporarily show the Android navigation buttons again.


Swiping up or Down
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  :class: todo-float-right
  
  LOW: FAQ Swiping up or Down

|FORCE-BREAK|

Showing the web page at the bottom of the throttle screen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo:: 
  :class: todo-float-right
  
  LOW: Showing the web page at the bottom of the throttle screen

See the Web Throttle view 

See the Web Throttle view preference  

<also point to the swipe up option>

Loco selection screen
--------------------------------------------

.. todo:: 
  :class: todo-float-right
  
  LOW: FAQ Loco selection screen

|FORCE-BREAK|

Locos in the roster not showing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  .. todo:: 
    :class: todo-float-right
    
    LOW: FAQ Locos in the roster not showing

  A1. check you don't have a filter 

  A2. ???

|FORCE-BREAK|

Changing the Connection screen
--------------------------------------------

Q. You can't remove test server by swiping right

  A. you can't remove it with a swipe, but there is a preference to remove it.  

  .. note:: 
    :class: note-ed-hidden-title

    See the `Hide Demo Server <../configuration/preferences.html#hide-demo-server>`_ preference for more information.

Changing the turnouts/Points screen
--------------------------------------------

.. todo:: 
  :class: todo-float-right
  
  LOW: FAQ Changing the turnouts screen

|FORCE-BREAK|

Conserving power on your phone/tablet
-------------------------------------

Q. My Phone/table runs out of power too quickly

  A. You should

  * Keep the brightness of the device/phone as low as practical
  * Disable Bluetooth and NFC if you are not using them
  * You can also try:

    * Set the :ref:`preference to dim screen on swipe up <configuration/preferences:swipe up-down preferences>`.  If you are not using the throttle temporarily (i.e the train does not need any control for a little while), dim the screen until you need it back.
    * Set the :ref:`preference to dim screen on shake <configuration/preferences:accelerometer (shake) preferences>`.  If you are not using the throttle temporarily (i.e the train does not need any control for a little while), dim the screen until you need it back.

  If your device has an AMOLED display, theoretically, the :ref:`High Contrast Outline theme <configuration/preferences:Theme/Style>` should use less power (though this is unproven).

.. note:: 
  :class: note-ed-hidden-title

  See the :doc:`../configuration/conserving_power` page for more information.


Virtual Sounds / In Phone Loco Sounds (IPLS)
--------------------------------------------

Q. I can't hear the In Phone Loco Sounds (IPLS)

  A. Adjust the 'Ring and Notification volume' in the Andrtoid System Settings. (the volume buttons on the side of the device/phone don't adjust this setting by default.)

  The IPLS feature of |ED| uses the Notification features of Android, not the Media Player features.

  That means that, at the Android system level, the volume is controlled by the 'Ring and Notification volume' not the 'Media volume'.

DCC-EX Features
--------------------------------------------

.. todo:: 
  :class: todo-float-right
  
  MEDIUM: FAQ DCC-EX Features

|FORCE-BREAK|