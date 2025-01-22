=============================
Quick Start / Getting Started
=============================

.. meta::
   :keywords: operation

.. include:: ../include.rst

* Install |ed| from the `Google Play Store <https://play.google.com/store/apps/details?id=jmri.enginedriver>`_ or by `direct download <../downloads/index.html>`_ of the .apk. 
* Confirm that your devices meet the `Prerequisites <../prerequisites/index.html>`_
* **Start your WiThrottle server**

  * For |JMRI|, Start the `WiThrottle <https://www.jmri.org/help/en/package/jmri/jmrit/withrottle/Protocol.shtml>`_ function of JMRI, located in *DecoderPro* under :menuselection:`Tools --> Start WiThrottle Server`. |br|\ It is also highly recommended that you start the `JMRI Web Server function <https://www.jmri.org/help/en/html/web/index.shtml>`_ :menuselection:`Tools -> Start JMRI Web Server`. 
  * For other server devices, turning them on and waiting a minute or two should be sufficient.

    See the `Prerequisites <../prerequisites/index.html>`_ page for more information.

  .. image:: ../_static/images/parts/network2.png
    :scale: 30 %
    :align: right

  .. image:: ../_static/images/parts/network1.png
    :scale: 35 %
    :align: right

* **On your Android device/phone** 
    
  * In you Android Device's system network and WiFi settings, make sure you are connected to same network as the network of the |WTS-DCC-EX|.

  |FORCE-BREAK|

  * Start |ED| 

    .. image:: ../_static/images/setup_wizard/setup1.png
       :scale: 7 %
       :align: right

    * The first time you run |ED| you will need to go through the Setup Wizard to agree to the permissions and select a few key preferences  
   
      See the `Setup Wizard <../configuration/setup_wizard.html>`_ page for more information.

  |FORCE-BREAK|

  * Wait for your |WTSS-DCC-EXS| to show up in 'Discovered Servers'

  * Click on the appropriate *Discovered server*

    .. image:: ../_static/images/parts/connecting_discovered_servers.png
       :scale: 30 %
       :align: right

    * If your |WTS-DCC-EX| does not show up, check that are on the same network as the |WTS-DCC-EX|.   
    * If the server *never* appears in the discovered list, type in the IP address and Port of the |WTS-DCC-EX| (Using the values shown on the JMRI WiThrottle window, or from the documentation for your server/Command Station) and press :guilabel:`Connect`. |br|\ Note: this situation is sometimes possible even if you are on the same network. |br|\ |br|\ See the `WiFi connection <./wifi_issues.html>`_ page for more assistance if you have connection issues. |br|\ |br|\ 

  |FORCE-BREAK|

  .. image:: ../_static/images/screenshots/power_dcc_ex.png
      :scale: 12 %
      :align: right

  .. image:: ../_static/images/parts/menu_throttle_dcc_ex_cut.png
      :scale: 11 %
      :align: right

  * If needed, turn the track power on with :menuselection:`Menu --> Power` and confirm the button is 'green'  (This is not required by all DCC Command Stations.)
  
  |FORCE-BREAK|

  .. image:: ../_static/images/parts/select_button.png
       :scale: 22 %
       :align: right

  * On the Throttle screen, click on the :guilabel:`Select` loco button
 
  |FORCE-BREAK|

  * On the next (Loco Select) screen, either:

    .. image:: ../_static/images/screenshots/select_dcc_address.png
        :scale: 81 %
        :align: right
        
    * Click on a loco from the Roster or Recent lists |BR| or
    * Enter the loco address (verify short or long), and press :guilabel:`Acquire`

      You will be returned to the |T-S|.

      For Consists / multiple units, see the note below.
 
  |FORCE-BREAK|

  .. image:: ../_static/images/screenshots/throttle_horizontal_outline_theme.png
      :scale: 7 %
      :align: right
        
  * Operate your loco 
  
    * Use the slider, or volume hardware buttons, or optional buttons for speed
    * Use the :guilabel:`Forward` and :guilabel:`Reverse` buttons to control direction
 
  |FORCE-BREAK|

  * Press your phone's Menu button :guilabel:`≡` to access screens for Turnout/Point, Route and Power control, as well as adjust settings and set numerous preferences
  * You can also 'swipe/fling' left or right to jump quickly back and forth between the Throttle, Routes, Turnouts/Points and Web pages. (Use Preferences to choose which are in the left / right swipe list) |br|\ |br|\ 

  * To release a single loco (or consist/multiple unit), click :guilabel:`Select` again and click the :guilabel:`Release` button

  * To release all locos, just press the :guilabel:`Back` button and exit the app. |br|\ This will also stop your locos (can be overridden in preferences)

Note:

* To create a consist/multiple unit 'on-the-fly', simply select additional locos for the same throttle, then select which way the new loco if facing. Direction and speed will be sent for all. :guilabel:`Release` will release all for that throttle.

