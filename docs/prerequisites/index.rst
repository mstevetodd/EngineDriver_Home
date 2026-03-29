*******************************************
Prerequisites for Using Engine Driver
*******************************************

.. meta::
   :keywords: prerequisites

.. include:: ../include.rst

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
     :local:

To Use Engine Driver You must...
---------------------------------

1. Have a Android device/phone. |BR| |ED| can only be installed on an Android device/phone (or an Android emulator on a PC.)

   *ALSO*
 
2. A compatible server (software or device) connected to your model train layout for |ed| to connect to. Either:

   a) A |WTS| |BR| **OR**
   b) A |EX-CS|.

Android Device/Phone
--------------------

.. image:: ../_static/images/screenshots/phones.png
   :scale: 15%
   :align: right

|ed| will work on most Android devices (Phones and Tablets) made in the last 5-6 years. Currently it has a minSDKVersion 21, which equates to minimum Android OS version of 5.0 (Lollipop). Info on minSDKVersion available in the `Engine Driver manifest <https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels>`_.

A number of :ref:`permissions <about/privacy-policy:required permissions>` are required to be granted to |ED| for it to function at its best, but as of Version 2.40.200 it will generally work without any additional permissions.

|FORCE-BREAK|

ESU Mobile Control Pro
"""""""""""""""""""""""
.. image:: ../_static/images/gamepads/esu_mcii.png
   :scale: 25 %
   :align: right

|ed| also fully supports the `ESU MobileControl Pro (MCPro) <http://www.esu.eu/en/products/digital-control/mobile-control-ii/>`_ Android throttle.

.. note:: 
  :class: note-ed-hidden-title
  
  See the `ESU MobileControl Pro <../operation/esu_mcii.html>`_ page for more information.

.. note:: 
  
  Support for the ESU MobileControl II (MCII) was dropped in Version 2.42.222 as it uses Android 4.
  
  Older versions of |ED| can still be downloaded from the :doc:`/downloads/index` page if you have an MCII and want to use it with |ED|.


|FORCE-BREAK|

WiThrottle and DCC-EX Native Servers
------------------------------------

|ED| can connect to a number of different |SERVERS|.  Information for some of them is provided below.

For JMRI
""""""""

.. image:: ../_static/images/wit_servers/jmri_withrottle_window.png
  :align: right
  :scale: 50%

Verify your Android device can connect to your network via WiFi and obtain an IP address.
Make sure you are running one of the latest versions of `JMRI <https://jmri.org/>`_ (5.0 or greater) on your PC or RPi, connected to your layout. 
Start up |JMRI| and verify you can use JMRI's included 'Throttle' window to control a loco on your layout.

Start the `WiThrottle <https://www.jmri.org/help/en/package/jmri/jmrit/withrottle/Protocol.shtml>`_ function of JMRI, located in DecoderPro under :menuselection:`Tools --> Throttles`.  

It is also highly recommended that you start the `JMRI Web Server function <https://www.jmri.org/help/en/html/web/index.shtml>`_ (:menuselection:`Tools --> Start JMRI Web Server`). 
Both of these should be added to Preferences, Start Up as well (:menuselection:`Edit --> Preferences --> Start Up`).

.. image:: ../_static/images/jmri/jmri-dccpp-menu.png
   :scale: 60 %
   :align: right

Note that if you are using an |EX-CS| as your |CS|, connected to |JMRI|, it is recommended to enable the "DCC++ over TCP Server" in Decoder-Pro (:menuselection:`DCC++/DCC-EX --> DCC++ over TCP Server`).  This will give you access to the advanced features provided by the |NATIVE| in addition to the |WIT|.

|FORCE-BREAK|

For DCC-EX WiFi
"""""""""""""""

.. image:: ../_static/images/wit_servers/dcc_ex_mega.png
   :scale: 10 %
   :align: right
   
|EX-CS| includes a built-in `WiThrottle Server <https://dcc-ex.com/throttles/protocols.html#the-withrottle-server>`_. Build your `DCC-EX Command Station <https://dcc-ex.com/get-started/index.html>`_, add `WiFi <https://dcc-ex.com/get-started/wifi-setup.html>`_, then connect EngineDriver following `these steps <https://dcc-ex.com/throttles/protocols.html#the-withrottle-server>`_.

|ED| can communicate with |EX-CSS| using either |WIT| or the |NATIVE|. By default |ED| will use the |NATIVE| as long as the *name* of the server includes "DCC-EX" or "DCCEX" (upper or lower case) *or* the port is 2560.

For MRC WiFi
""""""""""""

Connect the `MRC WiFi module <https://www.modelrectifier.com/category-s/332.htm>`_, and verify your device can connect to its network and obtain an IP address.
Note for MRC users: David Fuller has provided some `additional setup information [here] <../_static/files/EngineDriver_App-MRC_Wi-Fi_Module_Settings.pdf>`_.

For Digitrax LnWi
"""""""""""""""""

Connect the `Digitrax LnWi <https://www.digitrax.com/products/wireless/lnwi/>`_, and verify your device can connect to its network and obtain an IP address.
