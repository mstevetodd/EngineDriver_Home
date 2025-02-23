*******************************************
About Engine Driver
*******************************************

.. include:: ../include.rst

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
      :local:

What is 'Engine Driver'
-----------------------

|EDT| (normally just referred to as |ed| or just **ED**) is a free Android application that connects to a `WiThrottle™ Server <https://jmri.org/help/en/package/jmri/jmrit/withrottle/UserInterface.shtml>`_ [#WIT]_  or `DCC-EX EX-CommandStation <https://dcc-ex.com/>`_ to control model trains. 

Supported |WTSS| include:

* |JMRI| (Using either the WiThrottle protocol or the Native DCC-EX protocol)
* |EX-CS| (Using either the WiThrottle protocol or the Native DCC-EX protocol)
* `MRC Prodigy WiFi <https://www.modelrectifier.com/category-s/332.htm>`_
* `Digitrax LnWi <https://www.digitrax.com/products/wireless/lnwi/>`_
* `WifiTrax (for NCE) <http://wifitrax.com/products/product-WFD-30-detail.html>`_ 

.. image:: ../_static/images/screenshots/throttle_horizontal_switching_colorful.png
   :scale: 8 %
   :align: right

|ed| can: 

* Control the speed direction and up to 32 DCC functions of your DCC enabled locos
* Up to six |locos_consists| can be controlled at the same time
* Easily create and edit on-the-fly |consists| (software-defined)
* Control layout power, turnouts/points, routes, and access JMRI web panels and windows
* :doc:`Play virtual loco sounds </configuration/ipls>` 
* Specific to the |EX-CS|, Engine Driver can also use the |NATIVE| to communicate which allows:
 
 * :ref:`Program CVs <operation/dcc-ex-native-protocol:Read and write DCC addresses on the Programming Track>` (Service Mode and Operation Mode)
 * Control the :ref:`TrackManager features <operation/dcc-ex-native-protocol:TrackManager control>`
 * Use some extended Route capabilities
 * Use the 'Request Loco ID' & 'Drive Away' feature from a Program track onto Mainline track

You can customise |ed| extensively to meet your needs.

Generally the |WTSS| that |ed| connects to are either |CSs|, or are designed to talk to |CSs| (e.g. |JMRI|) to subsequently talk to DCC Decoder equipped locos on a layout.  |EX-CS| also allows controlling DC locos [#DC]_ or even Slot cars instead.

.. note:: 
  :class: note-ed-hidden-title

  See the :doc:`/operation/index` page for details on how to use |ed|.

|ed| is open source software which is available on `github.com/JMRI/EngineDriver <https://github.com/JMRI/EngineDriver>`_. This documentation is also open source and can be accessed on `github.com/mstevetodd/EngineDriver_Home <https://github.com/mstevetodd/EngineDriver_Home>`_. Contribution to both the code and documentation is welcome.  See [`Contributing <../contributing/index.html>`_] for details.

|ed| currently has minSDKVersion of 16, which equates to minimum Android OS version of 4.1 (JELLYBEAN). 
Info on minSDKVersion available in the `Engine Driver manifest <https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels>`_.

 
.. [#DC] The |EX-CS| is capable of driving DC Pulse Width Modulation (PWM) outputs as well as, or instead of, DCC outputs.  |ED| is therefor capable of running DC locos as easily as it does DCC locos.

What's a 'WiThrottle Server'?
-----------------------------

**WiThrottle** stands for 'WiFi Throttle', and a 'WiThrottle Server' is just software running on your JMRI computer, DCC-EX EX-CommandStation, or dedicated device. It's called a 'Server' because it allows you to connect to it and it 'serves', or services, requests from another application. That application is called a 'Client'. So in this case |ed| is the client.

The **WiThrottle Protocol** itself is a standard for how WiFi throttles can communicate with the WiThrottle Server, much like the DCC standard is a standard for how data packets communicate with decoders. What this means for you, is that |ed| can talk to any WiThrottle compatible server, which in turn can talk to the DCC decoders in your locos.

.. note::
  :class: note-ed-hidden-title

  See the :ref:`WiThrottle / DCC-EX Native Servers <prerequisites/index:withrottle and dcc-ex native servers>` section of the Prerequisites page for information on the different WiThrottle Servers.

----

.. [#WIT] 'WiThrottle' is a trademark owned by Brett Hoffman. It is also an `iOS app <https://www.withrottle.com/html/home.html>`_ developed by Brett Hoffman which has similar capabilities to Engine Driver. |BR|\ The 'WiThrottle protocol' is a communications protocol developed by Brett Hoffman.  It is used by JMRI, |ed|, the WiThrottle app and a number of other apps and |CSs|. |BR|\ References in this website to a '|WTS|', refer to a server that can communicate using the 'WiThrottle protocol'.


WiThrottle protocol VS DCC-EX Native protocol
---------------------------------------------

|ED| traditionally used the WiThrottle Protocol (described above). When the |DCC-EX| team designed the |EX-CS| they found the WiThrottle Protocol too limiting and came up with a new protocol referred to originally as **DCC++** but later as **Native DCC-EX Protocol**.

|ED| can use either protocol and, by default, will try to use the more powerful **Native DCC-EX Protocol** when connecting to a |EX-CS|.

|ED| can also use the Native DCC-EX Protocol to connect to a |EX-CS| via |JMRI| but you need to enable the "DCC++ over TCP Server" in the "DCC++" or "DCC-EX" menu in Decoder-Pro.

Where can I get Engine Driver
-----------------------------

The current published version is available in the `Google Play Store <https://play.google.com/store/apps/details?id=jmri.enginedriver>`_ or by `direct download of the .apk file <../_static/apk/EngineDriver.apk>`_.

APK files for manual installation (including older versions) are available from the :doc:`Downloads page </downloads/index>`.

Roadmap
-----------

|ed| doesn't really have a roadmap.  Code changes (bug fixes and features) are done depending on several factors, including:

* Who is available to work on it 
* Who among the available people is interested enough to do the work
* Are there enough people likely to use it to make it worth the effort

At the moment there are only a few of us doing any work on |ed|, so things happen when they happen.

See the :doc:`/contact/index` page if you are having problems or wish to make a suggestion.

Alternates to Engine Driver
---------------------------

|ed| is not the only app that can connect to JMRI, |WTSS| or |EX-CSS|, so it is worth your time to investigate the alternates.

See the `JMRI WiThrottle page <https://www.jmri.org/help/en/package/jmri/jmrit/withrottle/UserInterface.shtml>`_ for a list of similar or related apps.

See the `DCC-EX page <https://dcc-ex.com/throttles/index.html>`_ for a list of similar or related apps.
