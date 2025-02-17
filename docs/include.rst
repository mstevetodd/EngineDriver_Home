.. meta::
   :description: JMRI Engine Driver Throttle
   :keywords: DCC Engine Driver EngineDriver JMRI manual help model railroad railway train 
..
.. |BR| raw:: html

   <br />
..
.. |small-start| raw:: html

    <span style="font-size: 75%">
..
.. |small-end| raw:: html

    </span>
..
.. |hr-dotted| raw:: html

   <hr class="hr-dotted" />
..
.. |hr-dashed| raw:: html

   <hr class="hr-dashed" />
..
.. |hr-heavy| raw:: html

   <hr class="hr-heavy" />
..
.. |hr-double| raw:: html

   <hr class="hr-double" />
..
.. |force-break| raw:: html

  <div style="display:block; box-sizing: border-box; clear: both;"> </div>
..
.. |ED| raw:: html
   
   <span style="font-weight: bold; font-style: italic; font-size: 110%; color: #db4700;">Engine&nbsp;Driver</span>
..
.. |EDs| raw:: html
   
   <span style="font-weight: bold; font-style: italic; font-size: 110%; color: #db4700;">Engine&nbsp;Driver's</span>
..
.. |EDT| raw:: html
   
   <span style="font-weight: bold; font-style: italic; font-size: 110%; color: #db4700;">Engine&nbsp;Driver Throttle</span>
..
.. |JEDT| raw:: html
   
   <span style="font-weight: bold; font-style: italic; font-size: 110%; color: #db4700;">JMRI Engine&nbsp;Driver Throttle</span>
..
.. |WTS| replace:: 
   
   :ref:`WiThrottle Server<about/index:what's a 'withrottle server'?>`
..
.. |WTSS| replace:: 
   
   :ref:`WiThrottle Servers<about/index:what's a 'withrottle server'?>`
..
.. |WTS-DCC-EX| replace:: 
   
   :ref:`WiThrottle Server<about/index:what's a 'withrottle server'?>` or :ref:`DCC-EX Server<about/index:withrottle protocol vs dcc-ex native protocol>` 
..
.. |WTSS-DCC-EXS| replace:: 
   
   :ref:`WiThrottle Servers<about/index:what's a 'withrottle server'?>` or :ref:`DCC-EX Servers<about/index:withrottle protocol vs dcc-ex native protocol>` 
..
.. |EX-CS| raw:: html
   
   <a href="https://dcc-ex.com/">DCC-EX EX-CommandStation</a>

.. |EX-CSS| raw:: html
   
   <a href="https://dcc-ex.com/">DCC-EX EX-CommandStations</a>

.. |DCC-EX| raw:: html
   
   <a href="https://dcc-ex.com/">DCC-EX</a>

.. |JMRI| raw:: html
   
   <a href="https://jmri.org/">JMRI</a>

.. |NATIVE| replace::
   
   :ref:`Native DCC-EX Protocol <about/index:withrottle protocol vs dcc-ex native protocol>`

.. |NATIVE_SERVER| replace::

   :ref:`DCC-EX Native Protocol server <about/index:withrottle protocol vs dcc-ex native protocol>`

.. |WIT| replace::

   :ref:`WiThrottle Protocol <about/index:what's a 'withrottle server'?>`

.. |SERVER| replace::

   :abbr:`Command Station/Server (JMRI, EX-CommandStation, WiFTrax, LnWi, etc.)`

.. |SERVERS| replace::

   :abbr:`Command Stations/Servers (JMRI, EX-CommandStation, WiFTrax, LnWi, etc.)`

.. |CS| replace::

   :abbr:`DCC Command Station (NCE, DigiTrax, EX-CommandStation, etc.)`

.. |CSs| replace::

   :abbr:`DCC Command Stations (NCE, DigiTrax, EX-CommandStation, etc.)`

..
.. Use |ED|\ to remove the leading space if you need to follow it by a comma etc.
..
.. |TODO| raw:: html
   
   <span style="color:red">TODO</span>
..
.. |TBA| raw:: html
   
   <span style="color:red">TODO</span>
..
..
.. Screens ..............................................
..
.. |T-S| replace:: 
   
   :ref:`Throttle Screen <operation/interface:throttle screen>`
..
.. |TP-S| replace:: 
   
   :ref:`Turnouts/Points Screen <operation/interface:turnouts/points screen>`
..
.. |R-S| replace:: 
   
   :ref:`Routes Screen <operation/interface:routes screen>`
..
.. |WV-S| replace:: 
   
   :ref:`Web View Screen <operation/interface:web view screen>`
..
.. |LS-S| replace:: 
   
   :ref:`Loco Select Screen <operation/interface:loco select screen>`
..
.. |C-S| replace:: 
   
   :ref:`Connection Screen <operation/interface:connection screen>`
..
.. |ISW-S| replace:: 
   
   :ref:`Intro/Setup Wizard Screen <operation/interface:Intro/Setup Wizard Screen>`
..
.. |FD-S| replace:: 
   
   :ref:`Function Defaults Screen <operation/interface:Function Defaults Screen>`
..
.. |P-S| replace:: 
   
   :ref:`Preferences Screen <operation/interface:preferences screen>`
..
.. |DCC-EX-S| replace:: 
   
   :ref:`DCC-EX Screen <operation/interface:dcc-ex screen>`
..
.. Throttle Screens/layouts ...............................
..
.. |SRT-TS| replace::
   
    :doc:`/operation/semi-realistic-throttle`
..
.. ........................................................
..
.. |SRT| replace::
   
    :abbr:`SRT (Semi-Realistic Throttle)`
..
.. ........................................................
..
.. role:: hand-written
..
.. ........................................................
..
.. |loco_consist| replace::
   
   :abbr:`Loco or Consist / Multiple Unit (One or more locos being controlled by a single throttle)`
..
.. |locos_consists| replace::
   
   :abbr:`Locos or Consists / Multiple Units (One or more locos being controlled by a single throttle)`
..
.. |consist| replace::
   
   :abbr:`Consist / Multiple Unit (More than one loco being controlled by a single throttle)`
..
.. |consists| replace::
   
   :abbr:`Consists / Multiple Units (More than one loco being controlled by a single throttle)`
..
.. |roster| replace::
   
   :abbr:`Server Roster (list of locos supplied by the WiThrottle or DCC-EX server)`
..
.. |IPLS| replace::
   
   :doc:`In Phone Loco Sounds </configuration/ipls>` (IPLS)
..
.. |IPLS_SHORT| replace::
   
   :doc:`IPLS </configuration/ipls>` (IPLS)
