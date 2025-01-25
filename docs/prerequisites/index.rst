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
--------------------------------

1. Have a Android device/phone. |BR| |ED| can only be installed on an Android device/phone.

*ALSO*
 
2. a) A |WTS-DCC-EX| must be available on a device connected to your model train layout for |ED| to connect to.

**OR**

2. b) A |EX-CS| must be available on a device connected to your model train layout for |ed| to connect to.

Android Device/Phone
--------------------

|ed| will work on most Android devices (Phones and Tablets) made in the last 8-9 years. Currently it has a minSDKVersion 16, which equates to minimum Android OS version of 4.1 (JELLYBEAN) but Android versions greater than 5.0 are recommended. Info on minSDKVersion available in the `Engine Driver manifest <https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels>`_.

.. image:: ../_static/images/gamepads/esu_mcii.png
   :scale: 25 %
   :align: right

ESU MobileControl II
""""""""""""""""""""

|ed| also fully supports the `ESU MobileControl II (MC2) <http://www.esu.eu/en/products/digital-control/mobile-control-ii/>`_ Android throttle.

.. note:: 
  :class: note-ed-hidden-title
  
  See the `ESU MobileControl II <../operation/esu_mcii.html>`_ page for more information.

WiThrottle and DCC-EX Native Servers
------------------------------------

For JMRI
""""""""

.. image:: ../_static/images/wit_servers/jmri_withrottle_window.png
  :align: right
  :scale: 50%

Verify your Android device can connect to your network via WiFi and obtain an IP address.
Make sure you are running one of the latest versions of `JMRI <https://jmri.org/>`_ (4.20 or greater) on your PC, connected to your layout. 
Start up JMRI and verify you can use JMRI's included 'Throttle' window to control a loco on your layout.

Start the `WiThrottle <https://www.jmri.org/help/en/package/jmri/jmrit/withrottle/Protocol.shtml>`_ function of JMRI, located in DecoderPro under Tools, Throttles.  

It is also highly recommended that you start the `JMRI Web Server function <https://www.jmri.org/help/en/html/web/index.shtml>`_ (Tools, Start JMRI Web Server). 
Both of these should be added to Preferences, Start Up as well.

.. image:: ../_static/images/jmri/jmri-dccpp-menu.png
   :scale: 60 %
   :align: right

Note that if you are using an |EX-CS| as your command station connected to |JMRI| it is recommended to enable the "DCC++ over TCP Server" in the "DCC++"/"DCC-EX" menu on Decoder-Pro.  This will give you access to the advanced features provided by the |NATIVE| in addition to the |WIT|.

For DCC-EX WiFi
"""""""""""""""

|EX-CS| includes a built-in `WiThrottle Server <https://dcc-ex.com/throttles/protocols.html#the-withrottle-server>`_. Build your `DCC-EX Command Station <https://dcc-ex.com/get-started/index.html>`_, add `WiFi <https://dcc-ex.com/get-started/wifi-setup.html>`_, then connect EngineDriver following `these steps <https://dcc-ex.com/throttles/protocols.html#the-withrottle-server>`_.

|ED| can communicate with |EX-CSS| using either |WIT| or the |NATIVE|. By default |ED| will use the |NATIVE| as long as the name of the server includes "DCC-EX" or "DCCEX" (upper or lower case) *or* the port is 2560.

For MRC WiFi
""""""""""""

Connect the `MRC WiFi module <https://www.modelrectifier.com/category-s/332.htm>`_, and verify your device can connect to its network and obtain an IP address.
Note for MRC users: David Fuller has provided some `additional setup information [here] <../_static/EngineDriver_App-MRC_Wi-Fi_Module_Settings.pdf>`_.

For Digitrax LnWi
"""""""""""""""""

Connect the `Digitrax LnWi <https://www.digitrax.com/products/wireless/lnwi/>`_, and verify your device can connect to its network and obtain an IP address.
