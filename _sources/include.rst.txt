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
.. |hr-dashed| raw:: html

   <hr class="hr-dashed" />
..
.. |hr-heavy| raw:: html

   <hr class="hr-heavy" />
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
.. |WTS| raw:: html 
   
   <a href="../about/index.html#what-s-a-withrottle-server">WiThrottle Server</a>
..
.. |WTSS| raw:: html 
   
   <a href="../about/index.html#what-s-a-withrottle-server">WiThrottle Servers</a>
..
.. |WTS-DCC-EX| raw:: html 
   
   <a href="../about/index.html#what-s-a-withrottle-server">WiThrottle Server</a> or <a href="../about/index.html##withrottle-protocol-vs-dcc-ex-native-protocol">DCC-EX Server</a>
..
.. |WTSS-DCC-EXS| raw:: html 
   
   <a href="../about/index.html#what-s-a-withrottle-server">WiThrottle</a> or <a href="../about/index.html##withrottle-protocol-vs-dcc-ex-native-protocol">DCC-EX Servers</a>
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
.. role:: hand-written
..