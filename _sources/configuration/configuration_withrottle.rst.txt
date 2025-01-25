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

* `JMRI`_ 

   * Using |WIT|, or
   * Using |NATIVE|

* `DCC-EX EX-CommandStation WiFi`_

   * Using |WIT|, or
   * Using |NATIVE|

* `MRC Prodigy WiFi`_
* `Digitrax LnWi`_
* `WifiTrax (for NCE)`_


JMRI
^^^^

* Check your preferences/settings to insure you allow or disallow the control features desired. 
* If you've defined your turnouts/points and routes in a panel file, make sure to specify 'user names' for those you'd like to see listed on your throttle. 
* You can also 'filter' the turnouts shown using the WiThrottle->Filter Controls option in the WiThrottle window.
* Entering roster entries, and defining routes and turnouts on the server will all make your |ed| throttle more powerful and easier to use (though not required). 
* |ed| will show additional info if the JMRI Web Server is started (such as roster details and icon images).

.. image:: ../_static/images/jmri/jmri-dccpp-menu.png
   :scale: 50 %
   :align: right

* To use the |NATIVE| with |JMRI| you must ``Load DCC++ over TCP Server`` in the 'DCC-EX' menu in |JMRI|, then connect |ED| to the additional server that is presented.


DCC-EX EX-CommandStation WiFi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Refer to the `developer's instructions <https://dcc-ex.com/ex-commandstation/advanced-setup/supported-wifi/wifi-config.html>`_.

MRC Prodigy WiFi
^^^^^^^^^^^^^^^^

For MRC users: David Fuller has provided some :download:`additional setup information </_static/files/EngineDriver_App-MRC_Wi-Fi_Module_Settings.pdf>`.


Digitrax LnWi
^^^^^^^^^^^^^

Refer to the `Digitrax LnWi manufacture's instructions <https://www.digitrax.com/tsd/product/LNWI>`_.

WifiTrax (for NCE)
^^^^^^^^^^^^^^^^^^

Refer to the `WifiTrax manufacture's instructions <http://www.wifitrax.com/manuals/hardwareManuals.html>`_.



