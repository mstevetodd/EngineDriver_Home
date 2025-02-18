*******************************************
Engine Driver
*******************************************

.. include:: ./include.rst

.. toctree::
   :hidden:
   :includehidden:

   about/index
   prerequisites/index
   operation/index
   configuration/index

.. toctree::
   :hidden:
   :includehidden:
   :caption: Help & Support

   videos/index
   contact/index


.. toctree::
   :hidden:
   :includehidden:
   :caption: Get Engine Driver

   downloads/index
   changes/index

.. toctree::
   :hidden:
   :includehidden:
   :caption: Additional Info

   about/privacy-policy
   glossary/index
   contributing/index

----
  
|JEDT|, more commonly known as |ed|, is a free Android application that connects to a WiThrottle™ [#WIT]_ Server or `DCC-EX EX-CommandStation <https://dcc-ex.com/>`_ to control model trains. 

.. image:: ./_static/images/screenshots/throttle_vertical_outline.png
   :scale: 8 %
   :align: right

Supported servers include |JMRI|, |EX-CS|, `MRC Prodigy WiFi <https://www.modelrectifier.com/category-s/332.htm>`_, `Digitrax LnWi <https://www.digitrax.com/products/wireless/lnwi/>`_, and `WifiTrax (for NCE) <http://wifitrax.com/products/product-WFD-30-detail.html>`_. 
Once connected, you can control the speed direction and up to 32 DCC functions of your DCC enabled locomotives (locos). From one to six locos or |locos_consists| can be controlled at the same time.  
You can easily create and edit on-the-fly |consists| (software-defined). 
You can also control layout power, turnouts/points, routes, and access JMRI web panels and windows.

.. note:: 
  :class: note-ed-hidden-title
  
  See the :doc:`/about/index` page for more information. |BR|\ See the :doc:`/operation/index` page for details on how to use |ed|.


Why Use Engine Driver
---------------------

.. image:: ./_static/images/screenshots/throttle_buttons.png
   :align: left

You can use |ed| to operate your DCC or DC [#DC]_ model train layout without being physically tethered by any wires. This allows you to walk around your layout, following your trains and/or position yourself anywhere around your layout (e.g. at your favourite viewing position).

You can add additional |ed| controllers inexpensively using old Android phones or tablets, instead of proprietary controllers.  (You don't need to have a sim card in the phone.)

You only need to interact with JMRI and/or your |CS| directly when setting up or re-configuring your layout. Once configured, you do not need to interact with either JMRI or your |CS| directly while you are running your trains. 

----

.. [#WIT] 'WiThrottle' is a trademark owned by Brett Hoffman. It is also an `iOS app <https://www.withrottle.com/html/home.html>`_ developed by Brett Hoffman which has similar capabilities to |ed|. |BR|\ The 'WiThrottle protocol' is a communications protocol developed by Brett Hoffman.  It is used by JMRI, |ed|, the wiThrottle app and a number of other apps and |CSs|. |BR|\ References in this website to a '|WTS|', refer to a server that can communicate using the 'WiThrottle protocol'.
 
.. [#DC] The |EX-CS| is capable of driving DC Pulse Width Modulation (PWM) outputs as well as, or instead of, DCC outputs.  |ED| is therefor capable of running DC locos as easily as it does DCC locos.