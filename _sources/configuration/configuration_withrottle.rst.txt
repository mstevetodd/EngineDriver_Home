*******************************************
Configuring Your Server
*******************************************

.. meta::
   :keywords: configuration preferences

.. include:: ../include.rst

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
     :local:

|ED| can connect to a number of supported |WIT| and |NATIVE| servers including:

* |JMRI| 

   * Using |WIT|, or
   * Using |NATIVE|

* |EX-CS|

   * Using |WIT|, or
   * Using |NATIVE|

* MRC Prodigy WiFi
* Digitrax LnWi
* WifiTrax (for NCE)


JMRI
^^^^

* Check your preferences/settings to insure you allow or disallow the control features desired. 
* If you've defined your turnouts/points and routes in a panel file, make sure to specify 'user names' for those you'd like to see listed on your throttle. 
* You can also 'filter' the turnouts shown using the WiThrottle->Filter Controls option in the WiThrottle window.
* Entering roster entries, and defining routes and turnouts on the server will all make your |ed| throttle more powerful and easier to use (though not required). 
* |ed| will show additional info if the JMRI Web Server is started (such as roster details and icon images).
* To use the |NATIVE| with |JMRI| you must ``Load DCC== over TCP Server`` in the 'DCC-EX' menu in |JMRI|, then connect |ED| to the additional server that is presented.


DCC-EX WiFi
^^^^^^^^^^^

Refer to the `developer's instructions <https://dcc-ex.com/advanced-setup/wifi-config.html>`_.

MRC WiFi
^^^^^^^^

For MRC users: David Fuller has provided some `additional setup information <https://enginedriver.mstevetodd.com/sites/enginedriver.mstevetodd.com/files/EngineDriver_App-MRC_Wi-Fi_Module_Settings.pdf>`_.


Digitrax LnWi
^^^^^^^^^^^^^

Refer to the `Digitrax LnWi manufacture's instructions <https://www.digitrax.com/tsd/product/LNWI>`_.

WifiTrax
^^^^^^^^

Refer to the `WifiTrax manufacture's instructions <http://www.wifitrax.com/manuals/hardwareManuals.html>`_.



