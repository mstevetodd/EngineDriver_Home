=============================
Quick Start / Getting Started
=============================

.. meta::
   :keywords: operation

.. include:: ../include.rst

----

1. Confirm that your devices meet the :doc:`Prerequisites </prerequisites/index>`
2. Install |ed| from the `Google Play Store <https://play.google.com/store/apps/details?id=jmri.enginedriver>`_ or by `direct download <../downloads/index.html>`_ of the .apk. 
3. **Start your** |WTS| or |EX-CS|

  * For |JMRI|, Start the `WiThrottle <https://www.jmri.org/help/en/package/jmri/jmrit/withrottle/Protocol.shtml>`_ function of JMRI, located in *DecoderPro* under :menuselection:`Tools --> Start WiThrottle Server`. |BR|\ It is also highly recommended that you start the `JMRI Web Server function <https://www.jmri.org/help/en/html/web/index.shtml>`_ :menuselection:`Tools --> Start JMRI Web Server`. 
  * For other server devices, including the |EX-CS|, turning it on and waiting a minute or two should be sufficient.

  See the `Prerequisites <../prerequisites/index.html>`_ page for more information.

  .. image:: ../_static/images/parts/network2.png
    :scale: 40 %
    :align: right

  .. image:: ../_static/images/parts/network1.png
    :scale: 45 %
    :align: right

4. **On your Android device/phone** 
    
  a. In your Android Device's system network and WiFi settings, make sure you are connected to same network as the network of the |WTS-DCC-EX|.

  |FORCE-BREAK|

  b. Start |ED| 

    .. image:: ../_static/images/setup_wizard/setup1.png
       :scale: 13 %
       :align: right

    * The first time you run |ED| you will need to go through the Setup Wizard to agree to the :ref:`permissions <about/privacy-policy:Required Permissions>` and select a few key preferences  .
   
      See the `Setup Wizard <../configuration/setup_wizard.html>`_ page for more information.

  |FORCE-BREAK|

  c. Wait for your |WTSS-DCC-EXS| to show up in 'Discovered Servers'

  d. Tap on the appropriate *Discovered server*

    .. image:: ../_static/images/parts/connecting_discovered_servers.png
       :scale: 40 %
       :align: right

    * If your |WTS-DCC-EX| does not show up, check that are on the same network as the |WTS-DCC-EX|.   
    * If the server *never* appears in the discovered list, type in the IP address and Port of the |WTS-DCC-EX| (Using the values shown on the JMRI WiThrottle window, or from the documentation for your server/|CS|) and press :guilabel:`Connect`. |BR|\ Note: this situation is sometimes possible even if you are on the same network. |BR|\ |BR|\ See the `WiFi connection <./wifi_issues.html>`_ page for more assistance if you have connection issues. |BR|\ |BR|\ 

  |FORCE-BREAK|

  .. image:: ../_static/images/screenshots/power_dcc_ex.png
      :scale: 23 %
      :align: right

  .. image:: ../_static/images/parts/menu_throttle_dcc_ex_cut.png
      :scale: 18 %
      :align: right

  f. If needed, turn the track power on with :menuselection:`Menu --> Power` and confirm the button is 'green'  (This is not required by all |CSs|.)
  
  |FORCE-BREAK|

  .. image:: ../_static/images/parts/select_button.png
       :scale: 28 %
       :align: right

  * On the Throttle screen, press on the :guilabel:`Select` loco button
 
  |FORCE-BREAK|

  g. On the next (Loco Select) screen, either:

    .. image:: ../_static/images/screenshots/select_dcc_address.png
        :scale: 150 %
        :align: right
        
    * Tap on a loco from the |ROSTER| or Recent lists |BR| or
    * Enter the loco address (verify short or long), and press :guilabel:`Acquire`

      You will be returned to the |T-S|.

      For |consists|, see the note below.
 
  |FORCE-BREAK|

  .. image:: ../_static/images/screenshots/throttle_horizontal_outline_theme.png
      :scale: 12 %
      :align: right
        
  h. Operate your loco 
  
    * Use the slider, or volume hardware buttons, or optional buttons for speed
    * Use the :guilabel:`Forward` and :guilabel:`Reverse` buttons to control direction
 
  |FORCE-BREAK|

  i. Press your phone's Menu button :guilabel:`≡` to access screens for Turnout/Point, Route and Power control, as well as adjust settings and set numerous preferences

    * You can also 'swipe/fling' left or right to jump quickly back and forth between the Throttle, Routes, Turnouts/Points and Web pages. (Use Preferences to choose which are in the left / right swipe list) |BR|\ |BR|\ 

  j. To release a single loco (or |consist|), press :guilabel:`Select` again and press the :guilabel:`Release` button

  k. To release all locos, just press the :guilabel:`Back` button and exit the app. |BR|\ This will also stop your locos (can be overridden in preferences)

Note:

* To create a |consist| 'on-the-fly', simply select additional locos for the same throttle, then select which way the new loco if facing. Direction and speed will be sent for all. :guilabel:`Release` will release all for that throttle.

