## Oracle Metric recursive calls
* [Statistics Descriptions](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639)
* Case
  *  Hard Parsing
  * cache misses
    * the dictionary data is found in cache, a recursive call is not made and the data is read from cache directly   
  * dynamic storage extension
* V$SYSSTAT
  *  TIMED_STATISTICS initialization parameter is set to true
  *  CLASS column contains a number representing one or more statistics classes. 
     * 1, User
     * 2, Redo
     * 4, Enqueue
     * 8, Cache
     * 16, OS
     * 32, Real Application Clusters
     * 64, SQL
     * 128, Debug
###  Database Statistics Descriptions 

<table cellpadding="4" cellspacing="0" class="FormalWide" title="Database Statistics Descriptions" summary="This table includes the names, class, and description for several database statistics. A value of Y in the TIMED_STATISTICS column indicates that the statistic is only populated when the TIMED_STATISTICS initialization parameter is set to true." width="100%" frame="hsides" border="1" rules="rows">
                     <thead>
                        <tr align="left" valign="top">
                           <th align="left" valign="bottom" width="28%" id="d2274789e217">Name</th>
                           <th align="left" valign="bottom" width="8%" id="d2274789e220">Class</th>
                           <th align="left" valign="bottom" width="51%" id="d2274789e223">Description</th>
                           <th align="left" valign="bottom" width="14%" id="d2274789e226">TIMED_STATISTICS</th>
                        </tr>
                     </thead>
                     <tbody>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e231" headers="d2274789e217 ">
                              <p><a id="d2274789e233" class="indexterm-anchor"></a>application wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e231 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e231 d2274789e223 ">
                              <p>The total wait time (in centiseconds) for waits that belong to the Application wait class</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e231 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e248" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I955055"><a id="d2274789e250" class="indexterm-anchor"></a>background checkpoints completed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e248 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e248 d2274789e223 ">
                              <p>Number of checkpoints completed by the background process. This statistic is incremented when the background process successfully advances the thread checkpoint.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e248 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e265" headers="d2274789e217 ">
                              <p><a id="d2274789e267" class="indexterm-anchor"></a>background checkpoints started
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e265 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e265 d2274789e223 ">
                              <p>Number of checkpoints started by the background process. This statistic can be larger than "background checkpoints completed" if a new checkpoint overrides an incomplete checkpoint or if a checkpoint is currently under way. This statistic includes only checkpoints of the redo thread. It does not include:</p>
                              <ul style="list-style-type: disc;">
                                 <li>
                                    <p>Individual file checkpoints for operations such as offline or begin backup</p>
                                 </li>
                                 <li>
                                    <p>Foreground (user-requested) checkpoints (for example, performed by <code class="codeph">ALTER SYSTEM CHECKPOINT LOCAL</code> statements)
                                    </p>
                                 </li>
                              </ul>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e265 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e292" headers="d2274789e217 ">
                              <p><a id="d2274789e294" class="indexterm-anchor"></a>background timeouts
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e292 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e292 d2274789e223 ">
                              <p>This is a count of the times where a background process has set an alarm for itself and the alarm has timed out rather than the background process being posted by another process to do some work.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e292 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e309" headers="d2274789e217 ">
                              <p><a id="d2274789e311" class="indexterm-anchor"></a>branch node splits
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e309 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e309 d2274789e223 ">
                              <p>Number of times an index branch block was split because of the insertion of an additional value</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e309 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e326" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27827"><a id="d2274789e328" class="indexterm-anchor"></a>buffer is not pinned count
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e326 d2274789e220 ">
                              <p>72</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e326 d2274789e223 ">
                              <p>Number of times a buffer was free when visited. Useful only for internal debugging purposes.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e326 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e343" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27831"><a id="d2274789e345" class="indexterm-anchor"></a>buffer is pinned count
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e343 d2274789e220 ">
                              <p>72</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e343 d2274789e223 ">
                              <p>Number of times a buffer was pinned when visited. Useful only for internal debugging purposes.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e343 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e360" headers="d2274789e217 ">
                              <p><a id="d2274789e362" class="indexterm-anchor"></a>bytes received via SQL*Net from client
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e360 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e360 d2274789e223 ">
                              <p>Total number of bytes received from the client over Oracle Net Services</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e360 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e377" headers="d2274789e217 ">
                              <p><a id="d2274789e379" class="indexterm-anchor"></a>bytes received via SQL*Net from dblink
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e377 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e377 d2274789e223 ">
                              <p>Total number of bytes received from a database link over Oracle Net Services</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e377 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e394" headers="d2274789e217 ">
                              <p><a id="d2274789e396" class="indexterm-anchor"></a>bytes sent via SQL*Net to client
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e394 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e394 d2274789e223 ">
                              <p>Total number of bytes sent to the client from the foreground processes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e394 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e411" headers="d2274789e217 ">
                              <p><a id="d2274789e413" class="indexterm-anchor"></a>bytes sent via SQL*Net to dblink
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e411 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e411 d2274789e223 ">
                              <p>Total number of bytes sent over a database link</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e411 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e429" headers="d2274789e217 ">
                              <p><a id="d2274789e431" class="indexterm-anchor"></a>Cached Commit SCN referenced
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e429 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e429 d2274789e223 ">
                              <p>Useful only for internal debugging purposes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e429 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e446" headers="d2274789e217 ">
                              <p><a id="d2274789e448" class="indexterm-anchor"></a>calls to get snapshot scn: kcmgss
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e446 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e446 d2274789e223 ">
                              <p>Number of times a snapshot system change number (SCN) was allocated. The SCN is allocated at the start of a transaction.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e446 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e465" headers="d2274789e217 ">
                              <p><a id="d2274789e467" class="indexterm-anchor"></a>calls to kcmgas
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e465 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e465 d2274789e223 ">
                              <p>Number of calls to routine kcmgas to get a new SCN</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e465 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e482" headers="d2274789e217 ">
                              <p><a id="d2274789e484" class="indexterm-anchor"></a>calls to kcmgcs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e482 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e482 d2274789e223 ">
                              <p>Number of calls to routine kcmgcs to get a current SCN</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e482 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e499" headers="d2274789e217 ">
                              <p><a id="d2274789e501" class="indexterm-anchor"></a>calls to kcmgrs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e499 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e499 d2274789e223 ">
                              <p>Number of calls to routine kcsgrs to get a recent SCN</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e499 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e516" headers="d2274789e217 ">
                              <p><a id="d2274789e518" class="indexterm-anchor"></a>change write time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e516 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e516 d2274789e223 ">
                              <p>Elapsed redo write time for changes made to <code class="codeph">CURRENT</code> blocks in 10s of milliseconds.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e516 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e536" headers="d2274789e217 ">
                              <p><a id="d2274789e538" class="indexterm-anchor"></a>cleanouts and rollbacks - consistent read gets
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e536 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e536 d2274789e223 ">
                              <p>Number of consistent gets that require both block rollbacks and block cleanouts.</p>
                              <p><span class="bold">See Also:</span> <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26158">consistent gets</a>"</span></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e536 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e560" headers="d2274789e217 ">
                              <p><a id="d2274789e562" class="indexterm-anchor"></a>cleanouts only - consistent read gets
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e560 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e560 d2274789e223 ">
                              <p>Number of consistent gets that require only block cleanouts, no rollbacks.</p>
                              <p><span class="bold">See Also:</span> <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26158">consistent gets</a>"</span></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e560 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e584" headers="d2274789e217 ">
                              <p><a id="d2274789e586" class="indexterm-anchor"></a>cluster key scan block gets
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e584 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e584 d2274789e223 ">
                              <p>Number of blocks obtained in a cluster scan</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e584 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e601" headers="d2274789e217 ">
                              <p><a id="d2274789e603" class="indexterm-anchor"></a>cluster key scans
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e601 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e601 d2274789e223 ">
                              <p>Number of cluster scans that were started</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e601 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e618" headers="d2274789e217 ">
                              <p><a id="d2274789e620" class="indexterm-anchor"></a>cluster wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e618 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e618 d2274789e223 ">
                              <p>The total wait time (in centiseconds) for waits that belong to the Cluster wait class</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e618 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e636" headers="d2274789e217 ">
                              <p><a id="d2274789e638" class="indexterm-anchor"></a>cold recycle reads
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e636 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e636 d2274789e223 ">
                              <p>Number of buffers that were read through the least recently used end of the recycle cache with fast aging strategy</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e636 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e653" headers="d2274789e217 ">
                              <p><a id="d2274789e655" class="indexterm-anchor"></a>commit cleanout failures: block lost
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e653 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e653 d2274789e223 ">
                              <p>Number of times Oracle attempted a cleanout at commit but could not find the correct block due to forced write, replacement, or switch <code class="codeph">CURRENT</code></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e653 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e674" headers="d2274789e217 ">
                              <p><a id="d2274789e676" class="indexterm-anchor"></a>commit cleanout failures: buffer being written
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e674 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e674 d2274789e223 ">
                              <p>Number of times Oracle attempted a cleanout at commit, but the buffer was currently being written</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e674 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e693" headers="d2274789e217 ">
                              <p><a id="d2274789e695" class="indexterm-anchor"></a>commit cleanout failures: callback failure
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e693 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e693 d2274789e223 ">
                              <p>Number of times the cleanout callback function returns <code class="codeph">FALSE</code></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e693 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e714" headers="d2274789e217 ">
                              <p><a id="d2274789e716" class="indexterm-anchor"></a>commit cleanout failures: cannot pin
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e714 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e714 d2274789e223 ">
                              <p>Total number of times a commit cleanout was performed but failed because the block could not be pinned</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e714 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e733" headers="d2274789e217 ">
                              <p><a id="d2274789e735" class="indexterm-anchor"></a>commit cleanout failures: hot backup in progress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e733 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e733 d2274789e223 ">
                              <p>Number of times Oracle attempted block cleanout at commit during hot backup. The image of the block must be logged before the buffer can be made dirty.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e733 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e752" headers="d2274789e217 ">
                              <p><a id="d2274789e754" class="indexterm-anchor"></a>commit cleanout failures: write disabled
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e752 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e752 d2274789e223 ">
                              <p>Number of times a cleanout block at commit was performed but the writes to the database had been temporarily disabled</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e752 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e771" headers="d2274789e217 ">
                              <p><a id="d2274789e773" class="indexterm-anchor"></a>commit cleanouts
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e771 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e771 d2274789e223 ">
                              <p>Total number of times the cleanout block at commit function was performed</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e771 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e788" headers="d2274789e217 ">
                              <p><a id="d2274789e790" class="indexterm-anchor"></a>commit cleanouts successfully completed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e788 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e788 d2274789e223 ">
                              <p>Number of times the cleanout block at commit function completed successfully</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e788 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e805" headers="d2274789e217 ">
                              <p><a id="d2274789e807" class="indexterm-anchor"></a>commit nowait performed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e805 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e805 d2274789e223 ">
                              <p>The number of asynchronous commits that were actually performed. These commits did not wait for the commit redo to be flushed and be present on disk before returning.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e805 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e822" headers="d2274789e217 ">
                              <p><a id="d2274789e824" class="indexterm-anchor"></a>commit nowait requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e822 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e822 d2274789e223 ">
                              <p>The number of no-wait commit or asynchronous commit requests that were made either using SQL or the OCI transaction control API</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e822 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e840" headers="d2274789e217 ">
                              <p><a id="d2274789e842" class="indexterm-anchor"></a>Commit SCN cached
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e840 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e840 d2274789e223 ">
                              <p>Number of times the system change number of a commit operation was cached</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e840 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e857" headers="d2274789e217 ">
                              <p><a id="d2274789e859" class="indexterm-anchor"></a>commit wait/nowait performed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e857 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e857 d2274789e223 ">
                              <p>The number of asynchronous/synchronous commits that were actually performed</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e857 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e872" headers="d2274789e217 ">
                              <p><a id="d2274789e874" class="indexterm-anchor"></a>commit wait/nowait requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e872 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e872 d2274789e223 ">
                              <p>The number of no-wait or wait commits  that were made either using SQL or the OCI transaction control API</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e872 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e889" headers="d2274789e217 ">
                              <p><a id="d2274789e891" class="indexterm-anchor"></a>commit wait performed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e889 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e889 d2274789e223 ">
                              <p>The number of synchronous commits that were actually performed. These commits waited for the commit redo to be flushed and be present on disk before returning.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e889 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e906" headers="d2274789e217 ">
                              <p><a id="d2274789e908" class="indexterm-anchor"></a>commit wait requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e906 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e906 d2274789e223 ">
                              <p>The number of waiting or synchronous commit requests that were made either using SQL or the OCI transaction control API</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e906 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e923" headers="d2274789e217 ">
                              <p><a id="d2274789e925" class="indexterm-anchor"></a>concurrency wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e923 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e923 d2274789e223 ">
                              <p>The total wait time (in centiseconds) for waits that belong to the Concurrency wait class</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e923 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e940" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26148"><a id="d2274789e942" class="indexterm-anchor"></a>consistent changes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e940 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e940 d2274789e223 ">
                              <p>Number of times a user process has applied rollback entries to perform a consistent read on the block</p>
                              <p>Work loads that produce a great deal of consistent changes can consume a great deal of resources. The value of this statistic should be small in relation to the "consistent gets" statistic.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e940 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e959" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26158"><a id="d2274789e961" class="indexterm-anchor"></a>consistent gets
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e959 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e959 d2274789e223 ">
                              <p>Number of times a consistent read was requested for a block.</p>
                              <p><span class="bold">See Also: </span><span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26148">consistent changes</a>"</span> and <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I28932">session logical reads</a>"</span> statistics
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e959 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e987" headers="d2274789e217 ">
                              <p><a id="d2274789e989" class="indexterm-anchor"></a>consistent gets direct
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e987 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e987 d2274789e223 ">
                              <p>Number of times a consistent read was requested for a block bypassing the buffer cache (for example, direct load operation). This is a subset of "consistent gets" statistics value.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e987 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1004" headers="d2274789e217 ">
                              <p><a id="d2274789e1006" class="indexterm-anchor"></a>consistent gets from cache
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1004 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1004 d2274789e223 ">
                              <p>Number of times a consistent read was requested for a block from buffer cache. This is a subset of "consistent gets" statistics value.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1004 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1021" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26169"><a id="d2274789e1023" class="indexterm-anchor"></a>CPU used by this session
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1021 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1021 d2274789e223 ">
                              <p>Amount of CPU time (in 10s of milliseconds) used by a session from the time a user call starts until it ends. If a user call completes within 10 milliseconds, the start and end user-call time are the same for purposes of this statistics, and 0 milliseconds are added.</p>
                              <p>A similar problem can exist in the reporting by the operating system, especially on systems that suffer from many context switches.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1021 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1041" headers="d2274789e217 ">
                              <p><a id="d2274789e1043" class="indexterm-anchor"></a>CPU used when call started
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1041 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1041 d2274789e223 ">
                              <p>The CPU time used when the call is started</p>
                              <p><span class="bold">See Also:</span> <span class="q">" <a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26169">CPU used by this session</a>"</span> 
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1041 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1067" headers="d2274789e217 ">
                              <p><a id="d2274789e1069" class="indexterm-anchor"></a>CR blocks created
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1067 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1067 d2274789e223 ">
                              <p>Number of <code class="codeph">CURRENT</code> blocks cloned to create CR (consistent read) blocks. The most common reason for cloning is that the buffer is held in a incompatible mode.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1067 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1087" headers="d2274789e217 ">
                              <p><a id="d2274789e1089" class="indexterm-anchor"></a>current blocks converted for CR
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1087 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1087 d2274789e223 ">
                              <p>Number <code class="codeph">CURRENT</code> blocks converted to CR state
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1087 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1107" headers="d2274789e217 ">
                              <p><a id="d2274789e1109" class="indexterm-anchor"></a>cursor authentications
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1107 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1107 d2274789e223 ">
                              <p>Number of privilege checks conducted during execution of an operation</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1107 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1124" headers="d2274789e217 ">
                              <p><a id="d2274789e1126" class="indexterm-anchor"></a>data blocks consistent reads - undo records applied
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1124 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1124 d2274789e223 ">
                              <p>Number of undo records applied to data blocks that have been rolled back for consistent read purposes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1124 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1141" headers="d2274789e217 ">
                              <p><a id="d2274789e1143" class="indexterm-anchor"></a>data warehousing cooling action
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1141 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1141 d2274789e223 ">
                              <p>Number of times that cooling occurred on this instance</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1141 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1158" headers="d2274789e217 ">
                              <p><a id="d2274789e1160" class="indexterm-anchor"></a>data warehousing evicted objects
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1158 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1158 d2274789e223 ">
                              <p>Number of times that objects got evicted by automatic big table caching on this instance</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1158 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1175" headers="d2274789e217 ">
                              <p><a id="d2274789e1177" class="indexterm-anchor"></a>data warehousing evicted objects - cooling
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1175 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1175 d2274789e223 ">
                              <p>Number of times that objects got evicted on this instance due to a cooling action</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1175 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1192" headers="d2274789e217 ">
                              <p><a id="d2274789e1194" class="indexterm-anchor"></a>data warehousing evicted objects - replace
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1192 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1192 d2274789e223 ">
                              <p>Number of times that objects got evicted due to caching replacement, that is, when an object is evicted because a hotter object forces it to be evicted from the cache</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1192 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1209" headers="d2274789e217 ">
                              <p><a id="d2274789e1211" class="indexterm-anchor"></a>data warehousing scanned blocks
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1209 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1209 d2274789e223 ">
                              <p>Number of blocks scanned by automatic big table caching on this instance using parallel query</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1209 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1226" headers="d2274789e217 ">
                              <p><a id="d2274789e1228" class="indexterm-anchor"></a>data warehousing scanned blocks - disk
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1226 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1226 d2274789e223 ">
                              <p>Number of blocks scanned by automatic big table caching on this instance by direct read from disk</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1226 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1244" headers="d2274789e217 ">
                              <p><a id="d2274789e1246" class="indexterm-anchor"></a>data warehousing scanned blocks - memory
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1244 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1244 d2274789e223 ">
                              <p>Number of blocks scanned by automatic big table caching on this instance by cache read from memory</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1244 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1261" headers="d2274789e217 ">
                              <p><a id="d2274789e1263" class="indexterm-anchor"></a>data warehousing scanned blocks - offload
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1261 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1261 d2274789e223 ">
                              <p>Number of blocks scanned by automatic big table caching on this instance by Exadata offloading</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1261 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1278" headers="d2274789e217 ">
                              <p><a id="d2274789e1280" class="indexterm-anchor"></a>data warehousing scanned objects
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1278 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1278 d2274789e223 ">
                              <p>Number of times the objects in automatic big table caching are scanned using parallel query</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1278 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1295" headers="d2274789e217 ">
                              <p><a id="d2274789e1297" class="indexterm-anchor"></a>db block changes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1295 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1295 d2274789e223 ">
                              <p>Closely related to <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26148">consistent changes</a>"</span>, this statistic counts the total number of changes that were part of an update or delete operation that were made to all blocks in the SGA. Such changes generate redo log entries and hence become permanent changes to the database if the transaction is committed.
                              </p>
                              <p>This approximates total database work. This statistic indicates the rate at which buffers are being dirtied (on a per-transaction or per-second basis, for example).</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1295 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1318" headers="d2274789e217 ">
                              <p><a id="d2274789e1320" class="indexterm-anchor"></a>db block gets
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1318 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1318 d2274789e223 ">
                              <p>Number of times a <code class="codeph">CURRENT</code> block was requested
                              </p>
                              <p><span class="bold">See Also:</span> <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26158">consistent gets</a>"</span></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1318 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1345" headers="d2274789e217 ">
                              <p><a id="d2274789e1347" class="indexterm-anchor"></a>db block gets direct
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1345 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1345 d2274789e223 ">
                              <p>Number of times a <code class="codeph">CURRENT</code> block was requested bypassing the buffer cache (for example, a direct load operation). This is a subset of "db block gets" statistics value.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1345 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1365" headers="d2274789e217 ">
                              <p><a id="d2274789e1367" class="indexterm-anchor"></a>db block gets from cache
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1365 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1365 d2274789e223 ">
                              <p>Number of times a <code class="codeph">CURRENT</code> block was requested from the buffer cache. This is a subset of "db block gets" statistics value.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1365 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1385" headers="d2274789e217 ">
                              <p><a id="d2274789e1387" class="indexterm-anchor"></a>DBWR checkpoint buffers written
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1385 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1385 d2274789e223 ">
                              <p>Number of buffers that were written for checkpoints</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1385 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1402" headers="d2274789e217 ">
                              <p><a id="d2274789e1404" class="indexterm-anchor"></a>DBWR checkpoints
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1402 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1402 d2274789e223 ">
                              <p>Number of times the DBWR was asked to scan the cache and write all blocks marked for a checkpoint or the end of recovery. This statistic is always larger than <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I955055">background checkpoints completed</a>"</span>.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1402 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1423" headers="d2274789e217 ">
                              <p><a id="d2274789e1425" class="indexterm-anchor"></a>DBWR lru scans
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1423 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1423 d2274789e223 ">
                              <p>Number of times that DBWR scans the LRU queue looking for buffers to write. This count includes scans to fill a batch being written for another purpose (such as a checkpoint).</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1423 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1440" headers="d2274789e217 ">
                              <p><a id="d2274789e1442" class="indexterm-anchor"></a>DBWR revisited being-written buffer
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1440 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1440 d2274789e223 ">
                              <p>Number of times that DBWR tried to save a buffer for writing and found that it was already in the write batch. This statistic measures the amount of "useless" work that DBWR had to do in trying to fill the batch.</p>
                              <p>Many sources contribute to a write batch. If the same buffer from different sources is considered for adding to the write batch, then all but the first attempt will be "useless" because the buffer is already marked as being written.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1440 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1460" headers="d2274789e217 ">
                              <p><a id="d2274789e1462" class="indexterm-anchor"></a>DBWR transaction table writes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1460 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1460 d2274789e223 ">
                              <p>Number of rollback segment headers written by DBWR. This statistic indicates how many "hot" buffers were written, causing a user process to wait while the write completed.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1460 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1477" headers="d2274789e217 ">
                              <p><a id="d2274789e1479" class="indexterm-anchor"></a>DBWR undo block writes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1477 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1477 d2274789e223 ">
                              <p>Number of rollback segment blocks written by DBWR</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1477 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1494" headers="d2274789e217 ">
                              <p><a id="d2274789e1496" class="indexterm-anchor"></a>DDL statements parallelized
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1494 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1494 d2274789e223 ">
                              <p>Number of DDL statements that were executed in parallel</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1494 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1511" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27758"><a id="d2274789e1513" class="indexterm-anchor"></a>deferred (CURRENT) block cleanout applications
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1511 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1511 d2274789e223 ">
                              <p>Number of times cleanout records are deferred, piggyback with changes, always current get</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1511 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1528" headers="d2274789e217 ">
                              <p><a id="d2274789e1530" class="indexterm-anchor"></a>DFO trees parallelized
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1528 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1528 d2274789e223 ">
                              <p>Number of times a serial execution plan was converted to a parallel plan</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1528 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1545" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26352"><a id="d2274789e1547" class="indexterm-anchor"></a>dirty buffers inspected
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1545 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1545 d2274789e223 ">
                              <p>Number of dirty buffers found by the user process while it is looking for a buffer to reuse</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1545 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1562" headers="d2274789e217 ">
                              <p><a id="d2274789e1564" class="indexterm-anchor"></a>DML statements parallelized
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1562 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1562 d2274789e223 ">
                              <p>Number of DML statements that were executed in parallel</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1562 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1579" headers="d2274789e217 ">
                              <p><a id="d2274789e1581" class="indexterm-anchor"></a>DML statements retried
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1579 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1579 d2274789e223 ">
                              <p>When a long-running DML is executing, the cursor may get  invalidated due to some concurrent DDL on one of the cursor's dependencies. In this case, an internal ORA-14403 error is thrown and is caught and cleared in one of the calling functions. The current work is rolled back and the DML is restarted without the user being notified of this.</p>
                              <p>The statistic counts the number of times that the thrown, caught, and cleared (ORA-14403) sequence occurred for DML statements. Should a DML vary widely in execution time, check this statistic to see if it increments during the DML execution. If so, then concurrent DDL may be the cause of the extra elapsed time.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1579 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1598" headers="d2274789e217 ">
                              <p><a id="d2274789e1600" class="indexterm-anchor"></a>enqueue conversions
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1598 d2274789e220 ">
                              <p>4</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1598 d2274789e223 ">
                              <p>Total number of conversions of the state of table or row lock</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1598 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1615" headers="d2274789e217 ">
                              <p><a id="d2274789e1617" class="indexterm-anchor"></a>enqueue deadlocks
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1615 d2274789e220 ">
                              <p>4</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1615 d2274789e223 ">
                              <p>Total number of deadlocks between table or row locks in different sessions</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1615 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1632" headers="d2274789e217 ">
                              <p><a id="d2274789e1634" class="indexterm-anchor"></a>enqueue releases
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1632 d2274789e220 ">
                              <p>4</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1632 d2274789e223 ">
                              <p>Total number of table or row locks released</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1632 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1650" headers="d2274789e217 ">
                              <p><a id="d2274789e1652" class="indexterm-anchor"></a>enqueue requests
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1650 d2274789e220 ">
                              <p>4</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1650 d2274789e223 ">
                              <p>Total number of table or row locks acquired</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1650 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1667" headers="d2274789e217 ">
                              <p><a id="d2274789e1669" class="indexterm-anchor"></a>enqueue timeouts
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1667 d2274789e220 ">
                              <p>4</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1667 d2274789e223 ">
                              <p>Total number of table and row locks (acquired and converted) that timed out before they could complete</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1667 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1684" headers="d2274789e217 ">
                              <p><a id="d2274789e1686" class="indexterm-anchor"></a>enqueue waits
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1684 d2274789e220 ">
                              <p>4</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1684 d2274789e223 ">
                              <p>Total number of waits that occurred during an enqueue convert or get because the enqueue get was deferred</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1684 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1701" headers="d2274789e217 ">
                              <p><a id="d2274789e1703" class="indexterm-anchor"></a>exchange deadlocks
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1701 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1701 d2274789e223 ">
                              <p>Number of times that a process detected a potential deadlock when exchanging two buffers and raised an internal, restartable error. Index scans are the only operations that perform exchanges.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1701 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1718" headers="d2274789e217 ">
                              <p><a id="d2274789e1720" class="indexterm-anchor"></a>execute count
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1718 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1718 d2274789e223 ">
                              <p>Total number of calls (user and recursive) that executed SQL statements</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1718 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1735" headers="d2274789e217 ">
                              <p><a id="d2274789e1737" class="indexterm-anchor"></a>fbda woken up
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1735 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1735 d2274789e223 ">
                              <p>Number of times the flashback data archive background process was woken up to do archiving</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1735 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1752" headers="d2274789e217 ">
                              <p><a id="d2274789e1754" class="indexterm-anchor"></a>file io wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1752 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1752 d2274789e223 ">
                              <p>Total time spent in wait (in microseconds) for I/O to datafiles, excluding the service time for such I/O. This is cumulative for all I/Os for all datafiles. The service time for one I/O operation is estimated as the minimum time spent in the I/O call seen so far. This service time is subtracted from the time spent in each I/O call to get the wait time for that I/O.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1752 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1769" headers="d2274789e217 ">
                              <p><a id="d2274789e1771" class="indexterm-anchor"></a>flash cache eviction: aged out
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1769 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1769 d2274789e223 ">
                              <p>Flash cache buffer is aged out of the Database Smart Flash Cache</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1769 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1786" headers="d2274789e217 ">
                              <p><a id="d2274789e1788" class="indexterm-anchor"></a>flash cache eviction: buffer pinned
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1786 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1786 d2274789e223 ">
                              <p>Database Smart Flash Cache buffer is invalidated due to object or range reuse, and so on. The Database Flash Cache Buffer was in use at the time of eviction.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1786 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1803" headers="d2274789e217 ">
                              <p><a id="d2274789e1805" class="indexterm-anchor"></a>flash cache eviction: invalidated
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1803 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1803 d2274789e223 ">
                              <p>Database Smart Flash Cache buffer is invalidated due to object or range reuse, and so on. The Database Smart Flash Cache buffer was not in use at the time of eviction.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1803 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1820" headers="d2274789e217 ">
                              <p><a id="d2274789e1822" class="indexterm-anchor"></a>flash cache insert skip: corrupt
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1820 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1820 d2274789e223 ">
                              <p>In-memory buffer was skipped for insertion into the Database Smart Flash Cache because the buffer was corrupted</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1820 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1838" headers="d2274789e217 ">
                              <p><a id="d2274789e1840" class="indexterm-anchor"></a>flash cache insert skip: DBWR overloaded
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1838 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1838 d2274789e223 ">
                              <p>In-memory buffer was skipped for insertion into the Database Smart Flash Cache because DBWR was busy writing other buffers</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1838 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1855" headers="d2274789e217 ">
                              <p><a id="d2274789e1857" class="indexterm-anchor"></a>flash cache insert skip: exists
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1855 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1855 d2274789e223 ">
                              <p>In-memory buffer was skipped for insertion into the Database Smart Flash Cache because it was already in the flash cache</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1855 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1872" headers="d2274789e217 ">
                              <p><a id="d2274789e1874" class="indexterm-anchor"></a>flash cache insert skip: modification
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1872 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1872 d2274789e223 ">
                              <p>In-memory buffer was skipped for insertion into the Database Smart Flash Cache because it was being modified</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1872 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1889" headers="d2274789e217 ">
                              <p><a id="d2274789e1891" class="indexterm-anchor"></a>flash cache insert skip: not current
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1889 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1889 d2274789e223 ">
                              <p>In-memory buffer was skipped for insertion into the Database Smart Flash Cache because it was not current</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1889 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1906" headers="d2274789e217 ">
                              <p><a id="d2274789e1908" class="indexterm-anchor"></a>flash cache insert skip: not useful
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1906 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1906 d2274789e223 ">
                              <p>In-memory buffer was skipped for insertion into the Database Smart Flash Cache because the type of buffer was not useful to keep</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1906 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1923" headers="d2274789e217 ">
                              <p><a id="d2274789e1925" class="indexterm-anchor"></a>flash cache inserts
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1923 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1923 d2274789e223 ">
                              <p>Total number of in-memory buffers inserted into the Database Smart Flash Cache</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1923 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1940" headers="d2274789e217 ">
                              <p><a id="d2274789e1942" class="indexterm-anchor"></a>flashback log write bytes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1940 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1940 d2274789e223 ">
                              <p>Total size in bytes of flashback database data written by RVWR to flashback database logs</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1940 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1957" headers="d2274789e217 ">
                              <p><a id="d2274789e1959" class="indexterm-anchor"></a>flashback log writes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1957 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1957 d2274789e223 ">
                              <p>Total number of writes by RVWR to flashback database logs</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1957 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1974" headers="d2274789e217 ">
                              <p><a id="d2274789e1976" class="indexterm-anchor"></a>foreground propagated tracked transactions
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1974 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1974 d2274789e223 ">
                              <p>Number of transactions modifying tables enabled for flashback data archive which were archived by a foreground process</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1974 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e1991" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I30175"><a id="d2274789e1993" class="indexterm-anchor"></a>free buffer inspected
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e1991 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e1991 d2274789e223 ">
                              <p>Number of buffers skipped over from the end of an LRU queue to find a reusable buffer. The difference between this statistic and <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26352">dirty buffers inspected</a>"</span> is the number of buffers that could not be used because they had a user, a waiter, or were being read or written, or because they were busy or needed to be written after rapid aging out.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e1991 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2012" headers="d2274789e217 ">
                              <p><a id="d2274789e2014" class="indexterm-anchor"></a>free buffer requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2012 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2012 d2274789e223 ">
                              <p>Number of times a reusable buffer or a free buffer was requested to create or load a block</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2012 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2030" headers="d2274789e217 ">
                              <p><a id="d2274789e2032" class="indexterm-anchor"></a>gc read wait failures
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2030 d2274789e220 ">
                              <p>40</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2030 d2274789e223 ">
                              <p>A read wait is when a CR server waits for a disk read to complete before serving a block to another instance. This statistic displays the number of times a read wait ended in failure, that is, after waiting it was unable to serve a block.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2030 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2047" headers="d2274789e217 ">
                              <p><a id="d2274789e2049" class="indexterm-anchor"></a>gc read wait timeouts
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2047 d2274789e220 ">
                              <p>40</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2047 d2274789e223 ">
                              <p>A read wait is when a CR server waits for a disk read to complete before serving a block to another instance. This statistic displays the number of times a read wait timed out, that is, the disk read did not complete in time, so the wait was aborted.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2047 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2064" headers="d2274789e217 ">
                              <p><a id="d2274789e2066" class="indexterm-anchor"></a>gc read waits
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2064 d2274789e220 ">
                              <p>40</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2064 d2274789e223 ">
                              <p>The number of times a CR server waited for a disk read, and then successfully served a block</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2064 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2081" headers="d2274789e217 ">
                              <p><a id="d2274789e2083" class="indexterm-anchor"></a>global enqueue CPU used by this session
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2081 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2081 d2274789e223 ">
                              <p>Amount of CPU time (in 10s of milliseconds) used by synchronous and asynchronous global enqueue activity in a session from the time a user call starts until it ends. If a user call completes within 10 milliseconds, the start and end user-call time are the same for purposes of this statistics, and 0 milliseconds are added.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2081 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2098" headers="d2274789e217 ">
                              <p><a id="d2274789e2100" class="indexterm-anchor"></a>global enqueue get time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2098 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2098 d2274789e223 ">
                              <p>Total elapsed time in 10s of milliseconds of all synchronous and asynchronous global enqueue gets and converts</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2098 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2115" headers="d2274789e217 ">
                              <p><a id="d2274789e2117" class="indexterm-anchor"></a>global enqueue gets async
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2115 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2115 d2274789e223 ">
                              <p>Total number of asynchronous global enqueue gets and converts</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2115 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2132" headers="d2274789e217 ">
                              <p><a id="d2274789e2134" class="indexterm-anchor"></a>global enqueue gets sync
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2132 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2132 d2274789e223 ">
                              <p>Total number of synchronous global enqueue gets and converts</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2132 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2149" headers="d2274789e217 ">
                              <p><a id="d2274789e2151" class="indexterm-anchor"></a>global enqueue releases
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2149 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2149 d2274789e223 ">
                              <p>Total number of synchronous global enqueue releases </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2149 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2166" headers="d2274789e217 ">
                              <p><a id="d2274789e2168" class="indexterm-anchor"></a>hot buffers moved to head of LRU
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2166 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2166 d2274789e223 ">
                              <p>When a hot buffer reaches the tail of its replacement list, Oracle moves it back to the head of the list to keep it from being reused. This statistic counts such moves.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2166 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2183" headers="d2274789e217 ">
                              <p><a id="d2274789e2185" class="indexterm-anchor"></a>immediate (CR) block cleanout applications
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2183 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2183 d2274789e223 ">
                              <p>Number of times cleanout records are applied immediately during consistent-read requests</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2183 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2200" headers="d2274789e217 ">
                              <p><a id="d2274789e2202" class="indexterm-anchor"></a>immediate (CURRENT) block cleanout applications
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2200 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2200 d2274789e223 ">
                              <p>Number of times cleanout records are applied immediately during current gets. Compare this statistic with <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27758">deferred (CURRENT) block cleanout applications</a>"</span></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2200 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2221" headers="d2274789e217 ">
                              <p><a id="d2274789e2223" class="indexterm-anchor"></a>IM default area resized
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2221 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2221 d2274789e223 ">
                              <p>The amount of memory by which the column store got resized</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2221 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2238" headers="d2274789e217 ">
                              <p><a id="d2274789e2240" class="indexterm-anchor"></a>IM populate accumulated time (ms)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2238 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2238 d2274789e223 ">
                              <p>Total amount of DB time (in milliseconds) spent populating CUs into the IM column store due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2238 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2255" headers="d2274789e217 ">
                              <p><a id="d2274789e2257" class="indexterm-anchor"></a>IM populate bytes in-memory EU data
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2255 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2255 d2274789e223 ">
                              <p>Size in bytes of in-memory EU data populated due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2255 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2272" headers="d2274789e217 ">
                              <p><a id="d2274789e2274" class="indexterm-anchor"></a>IM populate bytes uncompressed EU data
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2272 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2272 d2274789e223 ">
                              <p>Uncompressed size in bytes of in-memory EU data populated due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2272 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2289" headers="d2274789e217 ">
                              <p><a id="d2274789e2291" class="indexterm-anchor"></a>IM populate CUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2289 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2289 d2274789e223 ">
                              <p>Number of CUs populated in the IM column store due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2289 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2306" headers="d2274789e217 ">
                              <p><a id="d2274789e2308" class="indexterm-anchor"></a>IM populate CUs memcompress for capacity high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2306 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2306 d2274789e223 ">
                              <p>Number of CUs populated in the IM column store due to segment scans using memcompress for capacity high</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2306 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2323" headers="d2274789e217 ">
                              <p><a id="d2274789e2325" class="indexterm-anchor"></a>IM populate CUs memcompress for capacity low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2323 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2323 d2274789e223 ">
                              <p>Number of CUs populated in the IM column store due to segment scans using memcompress for capacity low</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2323 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2340" headers="d2274789e217 ">
                              <p><a id="d2274789e2342" class="indexterm-anchor"></a>IM populate CUs memcompress for dml
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2340 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2340 d2274789e223 ">
                              <p>Number of CUs populated in the IM column store due to segment scans using memcompress for DML</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2340 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2357" headers="d2274789e217 ">
                              <p><a id="d2274789e2359" class="indexterm-anchor"></a>IM populate CUs memcompress for query high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2357 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2357 d2274789e223 ">
                              <p>Number of CUs populated in the IM column store due to segment scans using memcompress for query high</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2357 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2374" headers="d2274789e217 ">
                              <p><a id="d2274789e2376" class="indexterm-anchor"></a>IM populate CUs memcompress for query low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2374 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2374 d2274789e223 ">
                              <p>Number of CUs populated in the IM column store due to segment scans using memcompress for query low</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2374 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2391" headers="d2274789e217 ">
                              <p><a id="d2274789e2393" class="indexterm-anchor"></a>IM populate CUs no memcompress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2391 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2391 d2274789e223 ">
                              <p>Number of CUs populated in the IM column store due to segment scans without compression</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2391 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2409" headers="d2274789e217 ">
                              <p><a id="d2274789e2411" class="indexterm-anchor"></a>IM populate CUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2409 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2409 d2274789e223 ">
                              <p>Number of CUs requested to be populated due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2409 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2426" headers="d2274789e217 ">
                              <p><a id="d2274789e2428" class="indexterm-anchor"></a>IM populate EUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2426 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2426 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2426 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2443" headers="d2274789e217 ">
                              <p><a id="d2274789e2445" class="indexterm-anchor"></a>IM populate EUs accumulated time (ms)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2443 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2443 d2274789e223 ">
                              <p>Total amount of DB time (in milliseconds) spent populating EUs into the IM column store due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2443 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2460" headers="d2274789e217 ">
                              <p><a id="d2274789e2462" class="indexterm-anchor"></a>IM populate EUs columns
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2460 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2460 d2274789e223 ">
                              <p>Number of columns populated in EUs due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2460 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2477" headers="d2274789e217 ">
                              <p><a id="d2274789e2479" class="indexterm-anchor"></a>IM populate EUs memcompress for capacity high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2477 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2477 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to segment scans at memcompress for capacity high</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2477 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2494" headers="d2274789e217 ">
                              <p><a id="d2274789e2496" class="indexterm-anchor"></a>IM populate EUs memcompress for capacity low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2494 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2494 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to segment scans at memcompress for capacity low</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2494 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2511" headers="d2274789e217 ">
                              <p><a id="d2274789e2513" class="indexterm-anchor"></a>IM populate EUs memcompress for dml
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2511 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2511 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to segment scans at memcompress for dml</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2511 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2528" headers="d2274789e217 ">
                              <p><a id="d2274789e2530" class="indexterm-anchor"></a>IM populate EUs memcompress for query high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2528 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2528 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to segment scans at memcompress for query high</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2528 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2545" headers="d2274789e217 ">
                              <p><a id="d2274789e2547" class="indexterm-anchor"></a>IM populate EUs memcompress for query low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2545 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2545 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to segment scans at memcompress for query low</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2545 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2562" headers="d2274789e217 ">
                              <p><a id="d2274789e2564" class="indexterm-anchor"></a>IM populate EUs no memcompress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2562 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2562 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store without compression due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2562 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2579" headers="d2274789e217 ">
                              <p><a id="d2274789e2581" class="indexterm-anchor"></a>IM populate EUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2579 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2579 d2274789e223 ">
                              <p>Number of EUs requested to be populated in the IM column store due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2579 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2597" headers="d2274789e217 ">
                              <p><a id="d2274789e2599" class="indexterm-anchor"></a>IM populate no contiguous inmemory space
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2597 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2597 d2274789e223 ">
                              <p>Number of CUs that fail to populate due to lack of contiguous space in In-Memory area</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2597 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2614" headers="d2274789e217 ">
                              <p><a id="d2274789e2616" class="indexterm-anchor"></a>IM populate segments
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2614 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2614 d2274789e223 ">
                              <p>Number of segments  populated due to segment scan</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2614 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2631" headers="d2274789e217 ">
                              <p><a id="d2274789e2633" class="indexterm-anchor"></a>IM populate segments requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2631 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2631 d2274789e223 ">
                              <p>Number of segments requested to be populated due to segment scan</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2631 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2648" headers="d2274789e217 ">
                              <p><a id="d2274789e2650" class="indexterm-anchor"></a>IM populate segments wall clock time (ms)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2648 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2648 d2274789e223 ">
                              <p>Total amount of wall clock time (in milliseconds) spent populating CUs into the IM column store due to segment scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2648 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2665" headers="d2274789e217 ">
                              <p><a id="d2274789e2667" class="indexterm-anchor"></a>IM prepopulate accumulated time (ms)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2665 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2665 d2274789e223 ">
                              <p>Total amount of DB time (in milliseconds) spent prepopulating CUs into the IM column store priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2665 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2682" headers="d2274789e217 ">
                              <p><a id="d2274789e2684" class="indexterm-anchor"></a>IM prepopulate bytes in-memory EU data
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2682 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2682 d2274789e223 ">
                              <p>Size in bytes of in-memory EU data populated due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2682 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2699" headers="d2274789e217 ">
                              <p><a id="d2274789e2701" class="indexterm-anchor"></a>IM prepopulate bytes uncompressed EU data
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2699 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2699 d2274789e223 ">
                              <p>Uncompressed size in bytes of in-memory EU data populated due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2699 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2716" headers="d2274789e217 ">
                              <p><a id="d2274789e2718" class="indexterm-anchor"></a>IM prepopulate CUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2716 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2716 d2274789e223 ">
                              <p>Number of CUs prepopulated in the IM column store due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2716 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2733" headers="d2274789e217 ">
                              <p><a id="d2274789e2735" class="indexterm-anchor"></a>IM prepopulate CUs memcompress for capacity high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2733 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2733 d2274789e223 ">
                              <p>Number of CUs prepopulated in the IM column store due to priority using memcompress for capacity high</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2733 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2750" headers="d2274789e217 ">
                              <p><a id="d2274789e2752" class="indexterm-anchor"></a>IM prepopulate CUs memcompress for capacity low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2750 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2750 d2274789e223 ">
                              <p>Number of CUs prepopulated in the IM column store due to priority using memcompress for capacity low</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2750 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2767" headers="d2274789e217 ">
                              <p><a id="d2274789e2769" class="indexterm-anchor"></a>IM prepopulate CUs memcompress for dml
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2767 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2767 d2274789e223 ">
                              <p>Number of CUs prepopulated in the IM column store due to priority using memcompress for DML</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2767 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2785" headers="d2274789e217 ">
                              <p><a id="d2274789e2787" class="indexterm-anchor"></a>IM prepopulate CUs memcompress for query high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2785 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2785 d2274789e223 ">
                              <p>Number of CUs prepopulated in the IM column store due to priority using memcompress for query high</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2785 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2802" headers="d2274789e217 ">
                              <p><a id="d2274789e2804" class="indexterm-anchor"></a>IM prepopulate CUs memcompress for query low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2802 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2802 d2274789e223 ">
                              <p>Number of CUs prepopulated in the IM column store due to priority using memcompress for query low</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2802 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2819" headers="d2274789e217 ">
                              <p><a id="d2274789e2821" class="indexterm-anchor"></a>IM prepopulate CUs no memcompress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2819 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2819 d2274789e223 ">
                              <p>Number of CUs prepopulated in the IM column store due to priority without compression</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2819 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2836" headers="d2274789e217 ">
                              <p><a id="d2274789e2838" class="indexterm-anchor"></a>IM prepopulate CUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2836 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2836 d2274789e223 ">
                              <p>Number of CUs requested to be prepopulated due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2836 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2853" headers="d2274789e217 ">
                              <p><a id="d2274789e2855" class="indexterm-anchor"></a>IM prepopulate EUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2853 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2853 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2853 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2870" headers="d2274789e217 ">
                              <p><a id="d2274789e2872" class="indexterm-anchor"></a>IM prepopulate EUs accumulated time (ms)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2870 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2870 d2274789e223 ">
                              <p>Total amount of DB time (in milliseconds) spent populating EUs into the IM column store due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2870 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2887" headers="d2274789e217 ">
                              <p><a id="d2274789e2889" class="indexterm-anchor"></a>IM prepopulate EUs columns
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2887 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2887 d2274789e223 ">
                              <p>Number of columns populated in EUs due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2887 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2904" headers="d2274789e217 ">
                              <p><a id="d2274789e2906" class="indexterm-anchor"></a>IM prepopulate EUs memcompress for capacity high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2904 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2904 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to priority at memcompress for capacity high</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2904 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2921" headers="d2274789e217 ">
                              <p><a id="d2274789e2923" class="indexterm-anchor"></a>IM prepopulate EUs memcompress for capacity low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2921 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2921 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to priority at memcompress for capacity low</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2921 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2938" headers="d2274789e217 ">
                              <p><a id="d2274789e2940" class="indexterm-anchor"></a>IM prepopulate EUs memcompress for dml
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2938 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2938 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to priority at memcompress for dml</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2938 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2955" headers="d2274789e217 ">
                              <p><a id="d2274789e2957" class="indexterm-anchor"></a>IM prepopulate EUs memcompress for query high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2955 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2955 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to priority at memcompress for query high</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2955 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2973" headers="d2274789e217 ">
                              <p><a id="d2274789e2975" class="indexterm-anchor"></a>IM prepopulate EUs memcompress for query low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2973 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2973 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store due to priority at memcompress for query low</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2973 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e2990" headers="d2274789e217 ">
                              <p><a id="d2274789e2992" class="indexterm-anchor"></a>IM prepopulate EUs no memcompress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e2990 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e2990 d2274789e223 ">
                              <p>Number of EUs populated in the IM column store without compression due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e2990 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3007" headers="d2274789e217 ">
                              <p><a id="d2274789e3009" class="indexterm-anchor"></a>IM prepopulate EUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3007 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3007 d2274789e223 ">
                              <p>Number of EUs requested to be populated in the IM column store due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3007 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3024" headers="d2274789e217 ">
                              <p><a id="d2274789e3026" class="indexterm-anchor"></a>IM prepopulate segments
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3024 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3024 d2274789e223 ">
                              <p>Number of segments  prepopulated due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3024 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3041" headers="d2274789e217 ">
                              <p><a id="d2274789e3043" class="indexterm-anchor"></a>IM prepopulate segments requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3041 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3041 d2274789e223 ">
                              <p>Number of segments requested to be prepopulated due to priority</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3041 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3058" headers="d2274789e217 ">
                              <p><a id="d2274789e3060" class="indexterm-anchor"></a>IM repopulate accumulated time (ms)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3058 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3058 d2274789e223 ">
                              <p>Total amount of DB time (in milliseconds) spent repopulating CUs into the IM column store due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3058 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3075" headers="d2274789e217 ">
                              <p><a id="d2274789e3077" class="indexterm-anchor"></a>IM repopulate bytes in-memory EU data
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3075 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3075 d2274789e223 ">
                              <p>Size in bytes of in-memory EU data repopulated due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3075 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3092" headers="d2274789e217 ">
                              <p><a id="d2274789e3094" class="indexterm-anchor"></a>IM repopulate CUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3092 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3092 d2274789e223 ">
                              <p>Total number of CUs requested to be repopulated due to CU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3092 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3109" headers="d2274789e217 ">
                              <p><a id="d2274789e3111" class="indexterm-anchor"></a>IM repopulate CUs memcompress for capacity high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3109 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3109 d2274789e223 ">
                              <p>Number of CUs repopulated in the IM column store using memcompress for capacity high due to CU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3109 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3126" headers="d2274789e217 ">
                              <p><a id="d2274789e3128" class="indexterm-anchor"></a>IM repopulate CUs memcompress for capacity low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3126 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3126 d2274789e223 ">
                              <p>Number of CUs repopulated in the IM column store using memcompress for capacity low due to CU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3126 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3143" headers="d2274789e217 ">
                              <p><a id="d2274789e3145" class="indexterm-anchor"></a>IM repopulate CUs memcompress for dml
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3143 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3143 d2274789e223 ">
                              <p>Number of CUs repopulated in the IM column store using memcompress for DML due to CU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3143 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3161" headers="d2274789e217 ">
                              <p><a id="d2274789e3163" class="indexterm-anchor"></a>IM repopulate CUs memcompress for query high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3161 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3161 d2274789e223 ">
                              <p>Number of CUs repopulated in the IM column store using memcompress for query high due to CU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3161 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3178" headers="d2274789e217 ">
                              <p><a id="d2274789e3180" class="indexterm-anchor"></a>IM repopulate CUs memcompress for query low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3178 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3178 d2274789e223 ">
                              <p>Number of Cus repopulated in the IM column store using memcompress for query low due to CU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3178 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3195" headers="d2274789e217 ">
                              <p><a id="d2274789e3197" class="indexterm-anchor"></a>IM repopulate CUs no memcompress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3195 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3195 d2274789e223 ">
                              <p>Number of CUs repopulated in the IM column store without compression due to CU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3195 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3212" headers="d2274789e217 ">
                              <p><a id="d2274789e3214" class="indexterm-anchor"></a>IM repopulate CUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3212 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3212 d2274789e223 ">
                              <p>Total number of CUs requested to be repopulated due to CU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3212 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3229" headers="d2274789e217 ">
                              <p><a id="d2274789e3231" class="indexterm-anchor"></a>IM repopulate (doublebuffering) CUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3229 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3229 d2274789e223 ">
                              <p>Number of CUs repopulated with double-buffering enabled on the earlier version of the CUs</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3229 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3246" headers="d2274789e217 ">
                              <p><a id="d2274789e3248" class="indexterm-anchor"></a>IM repopulate (doublebuffering) CUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3246 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3246 d2274789e223 ">
                              <p>Number of CUs requested to be repopulated with double-buffering enabled on the earlier version of the CUs</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3246 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3263" headers="d2274789e217 ">
                              <p><a id="d2274789e3265" class="indexterm-anchor"></a>IM repopulate EUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3263 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3263 d2274789e223 ">
                              <p>Number of EUs requested to be repopulated due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3263 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3280" headers="d2274789e217 ">
                              <p><a id="d2274789e3282" class="indexterm-anchor"></a>IM repopulate EUs accumulated time (ms)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3280 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3280 d2274789e223 ">
                              <p>Total amount of DB time (in milliseconds) spent repopulating EUs into the IM column store due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3280 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3297" headers="d2274789e217 ">
                              <p><a id="d2274789e3299" class="indexterm-anchor"></a>IM repopulate EUs columns
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3297 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3297 d2274789e223 ">
                              <p>Number of columns repopulated in EUs due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3297 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3314" headers="d2274789e217 ">
                              <p><a id="d2274789e3316" class="indexterm-anchor"></a>IM repopulate EUs memcompress for capacity high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3314 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3314 d2274789e223 ">
                              <p>Number of EUs repopulated in the IM column store at memcompress for capacity high due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3314 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3331" headers="d2274789e217 ">
                              <p><a id="d2274789e3333" class="indexterm-anchor"></a>IM repopulate EUs memcompress for capacity low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3331 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3331 d2274789e223 ">
                              <p>Number of EUs repopulated in the IM column store at memcompress for capacity low due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3331 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3349" headers="d2274789e217 ">
                              <p><a id="d2274789e3351" class="indexterm-anchor"></a>IM repopulate EUs memcompress for dml
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3349 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3349 d2274789e223 ">
                              <p>Number of EUs repopulated in the IM column store at memcompress for DML due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3349 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3366" headers="d2274789e217 ">
                              <p><a id="d2274789e3368" class="indexterm-anchor"></a>IM repopulate EUs memcompress for query high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3366 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3366 d2274789e223 ">
                              <p>Number of EUs repopulated in the IM column store at memcompress for query high due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3366 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3383" headers="d2274789e217 ">
                              <p><a id="d2274789e3385" class="indexterm-anchor"></a>IM repopulate EUs memcompress for query low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3383 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3383 d2274789e223 ">
                              <p>Number of EUs repopulated in the IM column store at memcompress for query low due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3383 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3400" headers="d2274789e217 ">
                              <p><a id="d2274789e3402" class="indexterm-anchor"></a>IM repopulate EUs no memcompress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3400 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3400 d2274789e223 ">
                              <p>Number of EUs repopulated in the IM column store without compression due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3400 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3417" headers="d2274789e217 ">
                              <p><a id="d2274789e3419" class="indexterm-anchor"></a>IM repopulate EUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3417 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3417 d2274789e223 ">
                              <p>Total number of EUs requested to be repopulated due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3417 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3434" headers="d2274789e217 ">
                              <p><a id="d2274789e3436" class="indexterm-anchor"></a>IM repopulate (incremental) CUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3434 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3434 d2274789e223 ">
                              <p>Number of CUs repopulated incrementally from earlier versions of the CUs</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3434 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3451" headers="d2274789e217 ">
                              <p><a id="d2274789e3453" class="indexterm-anchor"></a>IM repopulate (incremental) CUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3451 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3451 d2274789e223 ">
                              <p>Number of CUs requested to be repopulated incrementally from earlier versions of the CUs</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3451 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3468" headers="d2274789e217 ">
                              <p><a id="d2274789e3470" class="indexterm-anchor"></a>IM repopulate (incremental) EUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3468 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3468 d2274789e223 ">
                              <p>Number of EUs repopulated using unchanged data from the current EU due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3468 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3485" headers="d2274789e217 ">
                              <p><a id="d2274789e3487" class="indexterm-anchor"></a>IM repopulate (incremental) EUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3485 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3485 d2274789e223 ">
                              <p>Number of EUs requested to be repopulated using unchanged data from the current EU due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3485 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3502" headers="d2274789e217 ">
                              <p><a id="d2274789e3504" class="indexterm-anchor"></a>IM repopulate no contiguous inmemory space
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3502 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3502 d2274789e223 ">
                              <p>Number of CUs that failed to repopulate due to lack of contigunous space in In-Memory area</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3502 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3519" headers="d2274789e217 ">
                              <p><a id="d2274789e3521" class="indexterm-anchor"></a>IM repopulate (scan) CUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3519 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3519 d2274789e223 ">
                              <p>Number of CUs repopulated in the IM column store due to scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3519 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3537" headers="d2274789e217 ">
                              <p><a id="d2274789e3539" class="indexterm-anchor"></a>IM repopulate (scan) CUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3537 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3537 d2274789e223 ">
                              <p>Number of CUs requested to be repopulated in the IM column store due to scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3537 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3554" headers="d2274789e217 ">
                              <p><a id="d2274789e3556" class="indexterm-anchor"></a>IM repopulate (scan) EUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3554 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3554 d2274789e223 ">
                              <p>Number of EUs repopulated in the IM column store that were triggered by scans on the EU</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3554 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3571" headers="d2274789e217 ">
                              <p><a id="d2274789e3573" class="indexterm-anchor"></a>IM repopulate (scan) EUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3571 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3571 d2274789e223 ">
                              <p>Number of EUs requested for repopulation in the IM column store that were triggered by scans on the EU </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3571 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3588" headers="d2274789e217 ">
                              <p><a id="d2274789e3590" class="indexterm-anchor"></a>IM repopulate segments
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3588 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3588 d2274789e223 ">
                              <p>Number of segments repopulated</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3588 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3605" headers="d2274789e217 ">
                              <p><a id="d2274789e3607" class="indexterm-anchor"></a>IM repopulate segments requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3605 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3605 d2274789e223 ">
                              <p>Indicates the number of segments requested to be repopulated</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3605 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3622" headers="d2274789e217 ">
                              <p><a id="d2274789e3624" class="indexterm-anchor"></a>IM repopulate (trickle) accumulated time (ms)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3622 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3622 d2274789e223 ">
                              <p>Total amount of DB time (in milliseconds) spent trickle repopulating CUs into the IM column store due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3622 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3639" headers="d2274789e217 ">
                              <p><a id="d2274789e3641" class="indexterm-anchor"></a>IM repopulate (trickle) bytes in-memory EU data
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3639 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3639 d2274789e223 ">
                              <p>Size in bytes of in-memory EU data repopulated due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3639 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3656" headers="d2274789e217 ">
                              <p><a id="d2274789e3658" class="indexterm-anchor"></a>IM repopulate (trickle) bytes uncompressed EU data
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3656 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3656 d2274789e223 ">
                              <p>Uncompressed size in bytes of in-memory EU data repopulated due to EU reaching staleness threshold</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3656 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3673" headers="d2274789e217 ">
                              <p><a id="d2274789e3675" class="indexterm-anchor"></a>IM repopulate (trickle) CUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3673 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3673 d2274789e223 ">
                              <p>Number of CUs trickle repopulated in the IM column store due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3673 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3690" headers="d2274789e217 ">
                              <p><a id="d2274789e3692" class="indexterm-anchor"></a>IM repopulate (trickle) CUs memcompress for capacity high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3690 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3690 d2274789e223 ">
                              <p>Number of CUs trickle repopulated in the IM column store using memcompress for capacity high due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3690 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3707" headers="d2274789e217 ">
                              <p><a id="d2274789e3709" class="indexterm-anchor"></a>IM repopulate (trickle) CUs memcompress for capacity low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3707 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3707 d2274789e223 ">
                              <p>Number of CUs trickle repopulated in the IM column store using memcompress for capacity low due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3707 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3725" headers="d2274789e217 ">
                              <p><a id="d2274789e3727" class="indexterm-anchor"></a>IM repopulate (trickle) CUs memcompress for dml
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3725 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3725 d2274789e223 ">
                              <p>Number of CUs trickle repopulated in the IM column store using memcompress for DML due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3725 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3742" headers="d2274789e217 ">
                              <p><a id="d2274789e3744" class="indexterm-anchor"></a>IM repopulate (trickle) CUs memcompress for query high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3742 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3742 d2274789e223 ">
                              <p>Number of CUs trickle repopulated in the IM column store using memcompress for query high due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3742 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3759" headers="d2274789e217 ">
                              <p><a id="d2274789e3761" class="indexterm-anchor"></a>IM repopulate (trickle) CUs memcompress for query low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3759 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3759 d2274789e223 ">
                              <p>Number of CUs trickle repopulated in the IM column store using memcompress for query low due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3759 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3776" headers="d2274789e217 ">
                              <p><a id="d2274789e3778" class="indexterm-anchor"></a>IM repopulate (trickle) CUs no memcompress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3776 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3776 d2274789e223 ">
                              <p>Number of CUs trickle repopulated in the IM column store without compression due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3776 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3793" headers="d2274789e217 ">
                              <p><a id="d2274789e3795" class="indexterm-anchor"></a>IM repopulate (trickle) CUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3793 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3793 d2274789e223 ">
                              <p>Total number of CUs requested to be trickle repopulated due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3793 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3810" headers="d2274789e217 ">
                              <p><a id="d2274789e3812" class="indexterm-anchor"></a>IM repopulate (trickle) CUs resubmitted
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3810 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3810 d2274789e223 ">
                              <p>Number of CUs trickle repopulate tasks submitted</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3810 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3827" headers="d2274789e217 ">
                              <p><a id="d2274789e3829" class="indexterm-anchor"></a>IM repopulate (trickle) EUs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3827 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3827 d2274789e223 ">
                              <p>Number of EUs trickle repopulated in the IM column store due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3827 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3844" headers="d2274789e217 ">
                              <p><a id="d2274789e3846" class="indexterm-anchor"></a>IM repopulate (trickle) EUs accumulated time (ms)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3844 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3844 d2274789e223 ">
                              <p>Total amount of DB time (in milliseconds) spent trickle repopulating EUs into the IM column store due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3844 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3861" headers="d2274789e217 ">
                              <p><a id="d2274789e3863" class="indexterm-anchor"></a>IM repopulate (trickle) EUs columns
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3861 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3861 d2274789e223 ">
                              <p>Number of columns repopulated in EUs due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3861 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3878" headers="d2274789e217 ">
                              <p><a id="d2274789e3880" class="indexterm-anchor"></a>IM repopulate (trickle) EUs memcompress for capacity high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3878 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3878 d2274789e223 ">
                              <p>Number of EUs trickle repopulated in the IM column store due to DML changes at memcompress for capacity high</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3878 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3895" headers="d2274789e217 ">
                              <p><a id="d2274789e3897" class="indexterm-anchor"></a>IM repopulate (trickle) EUs memcompress for capacity low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3895 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3895 d2274789e223 ">
                              <p>Number of EUs trickle repopulated in the IM column store due to DML changes at memcompress for capacity low</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3895 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3913" headers="d2274789e217 ">
                              <p><a id="d2274789e3915" class="indexterm-anchor"></a>IM repopulate (trickle) EUs memcompress for dml
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3913 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3913 d2274789e223 ">
                              <p>Number of EUs trickle repopulated in the IM column store due to DML changes at memcompress for dml</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3913 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3930" headers="d2274789e217 ">
                              <p><a id="d2274789e3932" class="indexterm-anchor"></a>IM repopulate (trickle) EUs memcompress for query high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3930 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3930 d2274789e223 ">
                              <p>Number of EUs trickle repopulated in the IM column store due to DML changes at memcompress for query high</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3930 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3947" headers="d2274789e217 ">
                              <p><a id="d2274789e3949" class="indexterm-anchor"></a>IM repopulate (trickle) EUs memcompress for query low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3947 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3947 d2274789e223 ">
                              <p>Number of EUs trickle repopulated in the IM column store due to DML changes at memcompress for query low</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3947 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3964" headers="d2274789e217 ">
                              <p><a id="d2274789e3966" class="indexterm-anchor"></a>IM repopulate (trickle) EUs no memcompress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3964 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3964 d2274789e223 ">
                              <p>Number of EUs trickle repopulated in the IM column store without compression due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3964 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3981" headers="d2274789e217 ">
                              <p><a id="d2274789e3983" class="indexterm-anchor"></a>IM repopulate (trickle) EUs requested
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3981 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3981 d2274789e223 ">
                              <p>Number of EUs requested to be trickle repopulated in the IM column store due to DML changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3981 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e3998" headers="d2274789e217 ">
                              <p><a id="d2274789e4000" class="indexterm-anchor"></a>IM scan CUs column not in memory
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e3998 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e3998 d2274789e223 ">
                              <p>Number of extents that could not be read from the IM column store because one of the columns required was not in memory</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e3998 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4015" headers="d2274789e217 ">
                              <p><a id="d2274789e4017" class="indexterm-anchor"></a>IM scan CUs invalid or missing revert to on disk extent
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4015 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4015 d2274789e223 ">
                              <p>Number of extents where no IMCU exists</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4015 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4032" headers="d2274789e217 ">
                              <p><a id="d2274789e4034" class="indexterm-anchor"></a>IM scan CUs memcompress for query low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4032 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4032 d2274789e223 ">
                              <p>Number of memcompress for query high CUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4032 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4049" headers="d2274789e217 ">
                              <p><a id="d2274789e4051" class="indexterm-anchor"></a>IM scan CUs memcompress for query high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4049 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4049 d2274789e223 ">
                              <p>Number of memcompress for query high CUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4049 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4066" headers="d2274789e217 ">
                              <p><a id="d2274789e4068" class="indexterm-anchor"></a>IM scan CUs memcompress for capacity low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4066 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4066 d2274789e223 ">
                              <p>Number of memcompress for capacity low CUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4066 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4083" headers="d2274789e217 ">
                              <p><a id="d2274789e4085" class="indexterm-anchor"></a>IM scan CUs memcompress for capacity high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4083 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4083 d2274789e223 ">
                              <p>Number of memcompress for capacity high CUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4083 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4101" headers="d2274789e217 ">
                              <p><a id="d2274789e4103" class="indexterm-anchor"></a>IM scan CUs memcompress for dml
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4101 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4101 d2274789e223 ">
                              <p>Number of  memcompress for DML CUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4101 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4118" headers="d2274789e217 ">
                              <p><a id="d2274789e4120" class="indexterm-anchor"></a>IM scan CUs predicates applied
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4118 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4118 d2274789e223 ">
                              <p>Number of where clause predicates applied to the In-Memory storage index</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4118 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4135" headers="d2274789e217 ">
                              <p><a id="d2274789e4137" class="indexterm-anchor"></a>IM scan CUs predicates optimized
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4135 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4135 d2274789e223 ">
                              <p>Number of where clause predicates applied to the IM column store for which either all rows pass min/max pruning via an In-Memory storage index or no rows pass min/max pruning</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4135 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4152" headers="d2274789e217 ">
                              <p><a id="d2274789e4154" class="indexterm-anchor"></a>IM scan CUs pruned
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4152 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4152 d2274789e223 ">
                              <p>Number of CUs pruned by the storage index</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4152 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4169" headers="d2274789e217 ">
                              <p><a id="d2274789e4171" class="indexterm-anchor"></a>IM scan (dynamic) multi-threaded scans
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4169 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4169 d2274789e223 ">
                              <p>Number of In-Memory table scans which benefited from In-Memory dynamic scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4169 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4186" headers="d2274789e217 ">
                              <p><a id="d2274789e4188" class="indexterm-anchor"></a>IM scan (dynamic) tasks processed by parent
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4186 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4186 d2274789e223 ">
                              <p>Number of IMCUs processed normally because of Resource Manager limit</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4186 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4203" headers="d2274789e217 ">
                              <p><a id="d2274789e4205" class="indexterm-anchor"></a>IM scan (dynamic) tasks processed by thread
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4203 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4203 d2274789e223 ">
                              <p>Number of IMCUs processed in parallel by a worker thread</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4203 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4220" headers="d2274789e217 ">
                              <p><a id="d2274789e4222" class="indexterm-anchor"></a>IM scan (dynamic) rows
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4220 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4220 d2274789e223 ">
                              <p>Number of rows processed by In-Memory dynamic scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4220 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4237" headers="d2274789e217 ">
                              <p><a id="d2274789e4239" class="indexterm-anchor"></a>IM scan EU bytes in-memory
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4237 d2274789e220 ">
                              <p>128 </p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4237 d2274789e223 ">
                              <p>Size in bytes of in-memory EU data accessed by scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4237 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4254" headers="d2274789e217 ">
                              <p><a id="d2274789e4256" class="indexterm-anchor"></a>IM scan EU bytes uncompressed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4254 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4254 d2274789e223 ">
                              <p>Uncompressed size in bytes of in-memory EU data accessed by scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4254 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4271" headers="d2274789e217 ">
                              <p><a id="d2274789e4273" class="indexterm-anchor"></a>IM scan EU rows
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4271 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4271 d2274789e223 ">
                              <p>Number of rows scanned from EUs in the IM column store before where clause predicate applied</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4271 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4289" headers="d2274789e217 ">
                              <p><a id="d2274789e4291" class="indexterm-anchor"></a>IM scan EUs columns accessed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4289 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4289 d2274789e223 ">
                              <p>Number of columns in the EUs accessed by scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4289 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4306" headers="d2274789e217 ">
                              <p><a id="d2274789e4308" class="indexterm-anchor"></a>IM scan EUs columns decompressed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4306 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4306 d2274789e223 ">
                              <p>Number of columns in the EUs decompressed by scans</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4306 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4323" headers="d2274789e217 ">
                              <p><a id="d2274789e4325" class="indexterm-anchor"></a>IM scan EUs columns theoretical max
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4323 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4323 d2274789e223 ">
                              <p>Number of columns that would have been accessed from the EU if the scans looked at all columns</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4323 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4340" headers="d2274789e217 ">
                              <p><a id="d2274789e4342" class="indexterm-anchor"></a>IM scan EUs memcompress for capacity high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4340 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4340 d2274789e223 ">
                              <p>Number of memcompress for capacity high EUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4340 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4356" headers="d2274789e217 ">
                              <p><a id="d2274789e4358" class="indexterm-anchor"></a>IM scan EUs memcompress for capacity low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4356 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4356 d2274789e223 ">
                              <p>Number of memcompress for capacity low EUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4356 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4373" headers="d2274789e217 ">
                              <p><a id="d2274789e4375" class="indexterm-anchor"></a>IM scan EUs memcompress for dml
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4373 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4373 d2274789e223 ">
                              <p>Number of memcompress for DML EUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4373 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4390" headers="d2274789e217 ">
                              <p><a id="d2274789e4392" class="indexterm-anchor"></a>IM scan EUs memcompress for query high
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4390 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4390 d2274789e223 ">
                              <p>Number of memcompress for query high EUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4390 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4407" headers="d2274789e217 ">
                              <p><a id="d2274789e4409" class="indexterm-anchor"></a>IM scan EUs memcompress for query low
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4407 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4407 d2274789e223 ">
                              <p>Number of memcompress for query low EUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4407 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4424" headers="d2274789e217 ">
                              <p><a id="d2274789e4426" class="indexterm-anchor"></a>IM scan EUs no memcompress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4424 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4424 d2274789e223 ">
                              <p>Number of uncompressed EUs scanned in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4424 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4441" headers="d2274789e217 ">
                              <p><a id="d2274789e4443" class="indexterm-anchor"></a>IM scan EUs split pieces
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4441 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4441 d2274789e223 ">
                              <p>Number of split EU pieces among all IM EUs</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4441 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4458" headers="d2274789e217 ">
                              <p><a id="d2274789e4460" class="indexterm-anchor"></a>IM scan rows
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4458 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4458 d2274789e223 ">
                              <p>Number of rows in scanned In-Memory Compression Units (IMCUs)</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4458 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4476" headers="d2274789e217 ">
                              <p><a id="d2274789e4478" class="indexterm-anchor"></a>IM scan rows optimized
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4476 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4476 d2274789e223 ">
                              <p>Number of rows that were not scanned in the IM column store as they were pruned via a number of optimizations such as min/max pruning via In-Memory storage indexes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4476 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4493" headers="d2274789e217 ">
                              <p><a id="d2274789e4495" class="indexterm-anchor"></a>IM scan rows projected
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4493 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4493 d2274789e223 ">
                              <p>Number of rows returned from the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4493 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4510" headers="d2274789e217 ">
                              <p><a id="d2274789e4512" class="indexterm-anchor"></a>IM scan rows valid
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4510 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4510 d2274789e223 ">
                              <p>Number of rows scanned from the IM column store after applying valid vector</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4510 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4527" headers="d2274789e217 ">
                              <p><a id="d2274789e4529" class="indexterm-anchor"></a>IM scan segments minmax eligible
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4527 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4527 d2274789e223 ">
                              <p>Number of CUs that are eligible for min/max pruning via storage index</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4527 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4544" headers="d2274789e217 ">
                              <p><a id="d2274789e4546" class="indexterm-anchor"></a>IM space CU bytes allocated
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4544 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4544 d2274789e223 ">
                              <p>Number of In-Memory bytes allocated</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4544 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4561" headers="d2274789e217 ">
                              <p><a id="d2274789e4563" class="indexterm-anchor"></a>IM space CU creations initiated
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4561 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4561 d2274789e223 ">
                              <p>Number of space requests for CUs</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4561 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4578" headers="d2274789e217 ">
                              <p><a id="d2274789e4580" class="indexterm-anchor"></a>IM space CU extents allocated
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4578 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4578 d2274789e223 ">
                              <p>Number of In-Memory extents allocated</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4578 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4595" headers="d2274789e217 ">
                              <p><a id="d2274789e4597" class="indexterm-anchor"></a>IM space segments allocated
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4595 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4595 d2274789e223 ">
                              <p>Number of snapshot segments created</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4595 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4612" headers="d2274789e217 ">
                              <p><a id="d2274789e4614" class="indexterm-anchor"></a>IM space segments freed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4612 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4612 d2274789e223 ">
                              <p>Number of snapshot segments deleted</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4612 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4629" headers="d2274789e217 ">
                              <p><a id="d2274789e4631" class="indexterm-anchor"></a>IM transactions
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4629 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4629 d2274789e223 ">
                              <p>Number of transactions that triggered data to be journaled in the IM column store</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4629 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4646" headers="d2274789e217 ">
                              <p><a id="d2274789e4648" class="indexterm-anchor"></a>IM transactions CUs invalid
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4646 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4646 d2274789e223 ">
                              <p>Number of CUs in the IM column store invalidated by transactions</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4646 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4664" headers="d2274789e217 ">
                              <p><a id="d2274789e4666" class="indexterm-anchor"></a>IM transactions rows invalidated
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4664 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4664 d2274789e223 ">
                              <p>Number of rows in the IM column store invalidated by transactions</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4664 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4681" headers="d2274789e217 ">
                              <p><a id="d2274789e4683" class="indexterm-anchor"></a>IM transactions rows journaled
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4681 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4681 d2274789e223 ">
                              <p>Number of rows logged in the transaction journal</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4681 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4698" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BEIFFJAG"><a id="d2274789e4700" class="indexterm-anchor"></a>in call idle wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4698 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4698 d2274789e223 ">
                              <p>The total wait time (in microseconds) for waits that belong to the Idle wait class.</p>
                              <p><span class="bold">See Also:</span> <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BEIJDHBD">non-idle wait count</a>"</span> and <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BEICGIBJ">non-idle wait time</a>"</span></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4698 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4726" headers="d2274789e217 ">
                              <p><a id="d2274789e4728" class="indexterm-anchor"></a>index cmph cu, uncomp sentinels
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4726 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4726 d2274789e223 ">
                              <p>Number of CUs created with uncompressed sentinels</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4726 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4743" headers="d2274789e217 ">
                              <p><a id="d2274789e4745" class="indexterm-anchor"></a>index cmph dm, cu lock expand
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4743 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4743 d2274789e223 ">
                              <p>Number of times CU lock structure expanded</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4743 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4760" headers="d2274789e217 ">
                              <p><a id="d2274789e4762" class="indexterm-anchor"></a>index cmph dm, cu migrate row
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4760 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4760 d2274789e223 ">
                              <p>Number of times a row migrated from a CU</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4760 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4777" headers="d2274789e217 ">
                              <p><a id="d2274789e4779" class="indexterm-anchor"></a>index cmph dm, insert unpurge CU row
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4777 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4777 d2274789e223 ">
                              <p>Number of times a CU row was unpurged during insert</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4777 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4794" headers="d2274789e217 ">
                              <p><a id="d2274789e4796" class="indexterm-anchor"></a>index cmph dm, purge dummy CU
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4794 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4794 d2274789e223 ">
                              <p>Number of times dummy CU purged from leaf block</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4794 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4811" headers="d2274789e217 ">
                              <p><a id="d2274789e4813" class="indexterm-anchor"></a>index cmph dm, split for cu lock expand
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4811 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4811 d2274789e223 ">
                              <p>Number of times leaf block split for CU lock expansion</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4811 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4828" headers="d2274789e217 ">
                              <p><a id="d2274789e4830" class="indexterm-anchor"></a>index cmph dm, split for cu migrate row
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4828 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4828 d2274789e223 ">
                              <p>Number of leaf block splits due to CU row migration</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4828 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4845" headers="d2274789e217 ">
                              <p><a id="d2274789e4847" class="indexterm-anchor"></a>index cmph ld, CU fit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4845 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4845 d2274789e223 ">
                              <p>Number of times load created  a well sized CU, no space for uncompressed rows</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4845 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4863" headers="d2274789e217 ">
                              <p><a id="d2274789e4865" class="indexterm-anchor"></a>index cmph ld, CU fit, add rows
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4863 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4863 d2274789e223 ">
                              <p>Number of times load created a well sized CU, with space for uncompressed rows</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4863 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4880" headers="d2274789e217 ">
                              <p><a id="d2274789e4882" class="indexterm-anchor"></a>index cmph ld, CU negative comp
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4880 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4880 d2274789e223 ">
                              <p>Number of times load CU gave negative compression</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4880 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4897" headers="d2274789e217 ">
                              <p><a id="d2274789e4899" class="indexterm-anchor"></a>index cmph ld, CU over-est
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4897 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4897 d2274789e223 ">
                              <p>Number of times load created an oversized CU</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4897 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4914" headers="d2274789e217 ">
                              <p><a id="d2274789e4916" class="indexterm-anchor"></a>index cmph ld, CU under-est
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4914 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4914 d2274789e223 ">
                              <p>Number of times load created a small CU</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4914 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4931" headers="d2274789e217 ">
                              <p><a id="d2274789e4933" class="indexterm-anchor"></a>index cmph ld, infinite loop
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4931 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4931 d2274789e223 ">
                              <p>Number of times shrink CU attempts resulted in uncompressed rows</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4931 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4948" headers="d2274789e217 ">
                              <p><a id="d2274789e4950" class="indexterm-anchor"></a>index cmph ld, lf blks flushed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4948 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4948 d2274789e223 ">
                              <p>Number of leaf blocks flushed by load</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4948 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4965" headers="d2274789e217 ">
                              <p><a id="d2274789e4967" class="indexterm-anchor"></a>index cmph ld, lf blks w/ und CU
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4965 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4965 d2274789e223 ">
                              <p>Number of leaf blocks flushed with small CU</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4965 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4982" headers="d2274789e217 ">
                              <p><a id="d2274789e4984" class="indexterm-anchor"></a>index cmph ld, lf blks w/o CU
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4982 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4982 d2274789e223 ">
                              <p>Number of leaf blocks flushed without a CU</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4982 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e4999" headers="d2274789e217 ">
                              <p><a id="d2274789e5001" class="indexterm-anchor"></a>index cmph ld, lf blks w/o unc r
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e4999 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e4999 d2274789e223 ">
                              <p>Number of leaf blocks flushed without uncompressed rows</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e4999 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5016" headers="d2274789e217 ">
                              <p><a id="d2274789e5018" class="indexterm-anchor"></a>index cmph ld, retry in over-est
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5016 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5016 d2274789e223 ">
                              <p>Number of times CU was resized after creating an oversized CU</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5016 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5033" headers="d2274789e217 ">
                              <p><a id="d2274789e5035" class="indexterm-anchor"></a>index cmph ld, rows compressed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5033 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5033 d2274789e223 ">
                              <p>Number of rows compressed by load</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5033 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5051" headers="d2274789e217 ">
                              <p><a id="d2274789e5053" class="indexterm-anchor"></a>index cmph ld, rows uncompressed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5051 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5051 d2274789e223 ">
                              <p>Number of rows left uncompressed by load</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5051 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5068" headers="d2274789e217 ">
                              <p><a id="d2274789e5070" class="indexterm-anchor"></a>index cmph sc, ffs decomp buffers
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5068 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5068 d2274789e223 ">
                              <p>Number of blocks decompressed for fast scan</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5068 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5085" headers="d2274789e217 ">
                              <p><a id="d2274789e5087" class="indexterm-anchor"></a>index cmph sc, ffs decomp buffers released and found valid
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5085 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5085 d2274789e223 ">
                              <p>Number of times decompressed CU buffer was reused by fast scan</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5085 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5102" headers="d2274789e217 ">
                              <p><a id="d2274789e5104" class="indexterm-anchor"></a>index cmph sc, ffs decomp buffers rows avail
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5102 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5102 d2274789e223 ">
                              <p>Number of rows in decompressed buffer for fast scan</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5102 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5119" headers="d2274789e217 ">
                              <p><a id="d2274789e5121" class="indexterm-anchor"></a>index cmph sc, ffs decomp buffers rows used
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5119 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5119 d2274789e223 ">
                              <p>Number of rows used from decompressed buffer for fast scan</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5119 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5136" headers="d2274789e217 ">
                              <p><a id="d2274789e5138" class="indexterm-anchor"></a>index cmph sc, ffs decomp failures
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5136 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5136 d2274789e223 ">
                              <p>Number of time decompress CU was not possible for fast scan</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5136 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5153" headers="d2274789e217 ">
                              <p><a id="d2274789e5155" class="indexterm-anchor"></a></p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5153 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5153 d2274789e223 ">
                              <p>Number of times 90-10 leaf block CU splits were made 50-50</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5153 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5169" headers="d2274789e217 ">
                              <p><a id="d2274789e5171" class="indexterm-anchor"></a>index cmph sp, leaf norecomp limit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5169 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5169 d2274789e223 ">
                              <p>Number of times leaf block recompression reached the recompression limit</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5169 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5186" headers="d2274789e217 ">
                              <p><a id="d2274789e5188" class="indexterm-anchor"></a>index cmph sp, leaf norecomp negcomp
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5186 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5186 d2274789e223 ">
                              <p>Number of times leaf block recompression returned negative compression</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5186 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5203" headers="d2274789e217 ">
                              <p><a id="d2274789e5205" class="indexterm-anchor"></a>index cmph sp, leaf norecomp nospace
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5203 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5203 d2274789e223 ">
                              <p>Number of times leaf block recompression returned not enough space</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5203 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5220" headers="d2274789e217 ">
                              <p><a id="d2274789e5222" class="indexterm-anchor"></a>index cmph sp, leaf norecomp notry
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5220 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5220 d2274789e223 ">
                              <p>Number of times leaf block recompression not attempted</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5220 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5238" headers="d2274789e217 ">
                              <p><a id="d2274789e5240" class="indexterm-anchor"></a>index cmph sp, leaf norecomp oversize
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5238 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5238 d2274789e223 ">
                              <p>Number of times leaf block recompression returned an oversized CU</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5238 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5255" headers="d2274789e217 ">
                              <p><a id="d2274789e5257" class="indexterm-anchor"></a>index cmph sp, leaf norecomp zerocur
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5255 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5255 d2274789e223 ">
                              <p>Number of times leaf block recompression returned a CU with 0 rows</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5255 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5272" headers="d2274789e217 ">
                              <p><a id="d2274789e5274" class="indexterm-anchor"></a>index cmph sp, leaf recomp fewer ucs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5272 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5272 d2274789e223 ">
                              <p>Number of CUs created with reduced number of sentinels</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5272 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5289" headers="d2274789e217 ">
                              <p><a id="d2274789e5291" class="indexterm-anchor"></a>index cmph sp, leaf recomp zero ucs
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5289 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5289 d2274789e223 ">
                              <p>Number of CUs created with zero sentinels</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5289 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5306" headers="d2274789e217 ">
                              <p><a id="d2274789e5308" class="indexterm-anchor"></a>index cmph sp, leaf recompress
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5306 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5306 d2274789e223 ">
                              <p>Number of times a leaf block CU was recompressed</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5306 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5323" headers="d2274789e217 ">
                              <p><a id="d2274789e5325" class="indexterm-anchor"></a>index cmpl co, prefix mismatch
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5323 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5323 d2274789e223 ">
                              <p>Number of times reorg found a neighboring block prefix count mismatch</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5323 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5340" headers="d2274789e217 ">
                              <p><a id="d2274789e5342" class="indexterm-anchor"></a>index cmpl ro, blocks not compressed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5340 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5340 d2274789e223 ">
                              <p>Number of times prefix compression was not applied to avoid negative compression</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5340 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5357" headers="d2274789e217 ">
                              <p><a id="d2274789e5359" class="indexterm-anchor"></a>index cmpl ro, prefix change at block
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5357 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5357 d2274789e223 ">
                              <p>Number of times prefix count was changed to an optimal value</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5357 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5374" headers="d2274789e217 ">
                              <p><a id="d2274789e5376" class="indexterm-anchor"></a>index cmpl ro, prefix no change at block
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5374 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5374 d2274789e223 ">
                              <p>Number of times prefix count was already the optimal value</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5374 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5391" headers="d2274789e217 ">
                              <p><a id="d2274789e5393" class="indexterm-anchor"></a>index cmpl ro, reorg avoid load new block
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5391 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5391 d2274789e223 ">
                              <p>Number of times a block reorg avoided a new block being created during load</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5391 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5408" headers="d2274789e217 ">
                              <p><a id="d2274789e5410" class="indexterm-anchor"></a>index cmpl ro, reorg avoid split
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5408 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5408 d2274789e223 ">
                              <p>Number of times a block reorg avoided a block split during DML</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5408 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5426" headers="d2274789e217 ">
                              <p><a id="d2274789e5428" class="indexterm-anchor"></a>index fast full scans (direct read)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5426 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5426 d2274789e223 ">
                              <p>Number of fast full scans initiated using direct read</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5426 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5443" headers="d2274789e217 ">
                              <p><a id="d2274789e5445" class="indexterm-anchor"></a>index fast full scans (full)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5443 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5443 d2274789e223 ">
                              <p>Number of fast full scans initiated for full segments</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5443 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5460" headers="d2274789e217 ">
                              <p><a id="d2274789e5462" class="indexterm-anchor"></a>index fast full scans (rowid ranges)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5460 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5460 d2274789e223 ">
                              <p>Number of fast full scans initiated with rowid endpoints specified</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5460 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5477" headers="d2274789e217 ">
                              <p><a id="d2274789e5479" class="indexterm-anchor"></a>large tracked transactions
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5477 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5477 d2274789e223 ">
                              <p>For tables tracked by flashback data archive, the number of transactions modifying rows in those tables which are large in terms of size or number of changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5477 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5494" headers="d2274789e217 ">
                              <p><a id="d2274789e5496" class="indexterm-anchor"></a>leaf node splits
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5494 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5494 d2274789e223 ">
                              <p>Number of times an index leaf node was split because of the insertion of an additional value</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5494 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5511" headers="d2274789e217 ">
                              <p><a id="d2274789e5513" class="indexterm-anchor"></a>lob reads
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5511 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5511 d2274789e223 ">
                              <p>Number of LOB API read operations performed in the session/system. A single LOB API read may correspond to multiple physical/logical disk block reads.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5511 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5528" headers="d2274789e217 ">
                              <p><a id="d2274789e5530" class="indexterm-anchor"></a>lob writes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5528 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5528 d2274789e223 ">
                              <p>Number of LOB API write operations performed in the session/system. A single LOB API write may correspond to multiple physical/logical disk block writes.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5528 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5545" headers="d2274789e217 ">
                              <p><a id="d2274789e5547" class="indexterm-anchor"></a>lob writes unaligned
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5545 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5545 d2274789e223 ">
                              <p>Number of LOB API write operations whose start offset or buffer size is not aligned to the internal chunk size of the LOB. Writes aligned to chunk boundaries are the most efficient write operations. The internal chunk size of a LOB is available through the LOB API (for example, DBMS_LOB.GETCHUNKSIZE()).</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5545 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5562" headers="d2274789e217 ">
                              <p><a id="d2274789e5564" class="indexterm-anchor"></a>logons cumulative
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5562 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5562 d2274789e223 ">
                              <p>Total number of logons since the instance started. Useful only in V$SYSSTAT. It gives an instance overview of all processes that logged on.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5562 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5579" headers="d2274789e217 ">
                              <p><a id="d2274789e5581" class="indexterm-anchor"></a>logons current
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5579 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5579 d2274789e223 ">
                              <p>Total number of current logons. Useful only in V$SYSSTAT.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5579 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5596" headers="d2274789e217 ">
                              <p><a id="d2274789e5598" class="indexterm-anchor"></a> memopt r failed puts
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5596 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5596 d2274789e223 ">
                              <p>Total failed puts on hash index</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5596 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5614" headers="d2274789e217 ">
                              <p><a id="d2274789e5616" class="indexterm-anchor"></a> memopt r failed reads on blocks
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5614 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5614 d2274789e223 ">
                              <p>Total lookup failures due to read failure on blocks because of concurrent changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5614 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5631" headers="d2274789e217 ">
                              <p><a id="d2274789e5633" class="indexterm-anchor"></a> memopt r failed reads on buckets
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5631 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5631 d2274789e223 ">
                              <p>Total lookup failures due to concurrent hash bucket changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5631 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5648" headers="d2274789e217 ">
                              <p><a id="d2274789e5650" class="indexterm-anchor"></a> memopt r hits
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5648 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5648 d2274789e223 ">
                              <p>Total hits on hash index – primary key found</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5648 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5665" headers="d2274789e217 ">
                              <p><a id="d2274789e5667" class="indexterm-anchor"></a> memopt r lookup detected CR buffer
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5665 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5665 d2274789e223 ">
                              <p>Total lookup failures due to block pointed to by hash index being no longer the current version</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5665 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5682" headers="d2274789e217 ">
                              <p><a id="d2274789e5684" class="indexterm-anchor"></a> memopt r lookups
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5682 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5682 d2274789e223 ">
                              <p>Total number of lookups on hash index</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5682 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5699" headers="d2274789e217 ">
                              <p><a id="d2274789e5701" class="indexterm-anchor"></a> memopt r misses
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5699 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5699 d2274789e223 ">
                              <p>Total misses on hash index due to primary key not found</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5699 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5716" headers="d2274789e217 ">
                              <p><a id="d2274789e5718" class="indexterm-anchor"></a> memopt r puts
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5716 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5716 d2274789e223 ">
                              <p>Total puts on hash index</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5716 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5733" headers="d2274789e217 ">
                              <p><a id="d2274789e5735" class="indexterm-anchor"></a> memopt r successful puts
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5733 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5733 d2274789e223 ">
                              <p>Total successful puts on hash index</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5733 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5750" headers="d2274789e217 ">
                              <p><a id="d2274789e5752" class="indexterm-anchor"></a>messages received
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5750 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5750 d2274789e223 ">
                              <p>Number of messages sent and received between background processes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5750 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5767" headers="d2274789e217 ">
                              <p><a id="d2274789e5769" class="indexterm-anchor"></a>messages sent
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5767 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5767 d2274789e223 ">
                              <p>Number of messages sent and received between background processes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5767 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5784" headers="d2274789e217 ">
                              <p><a id="d2274789e5786" class="indexterm-anchor"></a>no buffer to keep pinned count
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5784 d2274789e220 ">
                              <p>72</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5784 d2274789e223 ">
                              <p>Number of times a visit to a buffer attempted, but the buffer was not found where expected. Like <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27827">buffer is not pinned count</a>"</span> and <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27831">buffer is pinned count</a>"</span>, this statistic is useful only for internal debugging purposes.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5784 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5810" headers="d2274789e217 ">
                              <p><a id="d2274789e5812" class="indexterm-anchor"></a>no work - consistent read gets
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5810 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5810 d2274789e223 ">
                              <p>Number consistent gets that require neither block cleanouts nor rollbacks.</p>
                              <p><span class="bold">See Also:</span> <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26158">consistent gets</a>"</span></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5810 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5834" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BEIJDHBD"><a id="d2274789e5836" class="indexterm-anchor"></a>non-idle wait count
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5834 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5834 d2274789e223 ">
                              <p>The total number of waits performed with wait events that were not part of the Idle wait class.</p>
                              <p><span class="bold">See Also:</span> <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BEIFFJAG">in call idle wait time</a>"</span> and <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BEICGIBJ">non-idle wait time</a>"</span></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5834 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5862" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BEICGIBJ"><a id="d2274789e5864" class="indexterm-anchor"></a>non-idle wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5862 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5862 d2274789e223 ">
                              <p>The total wait time (in microseconds) for waits that do not belong to the Idle wait class.</p>
                              <p><span class="bold">See Also:</span> <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BEIFFJAG">in call idle wait time</a>"</span> and <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BEIJDHBD">non-idle wait count</a>"</span></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5862 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5890" headers="d2274789e217 ">
                              <p><a id="d2274789e5892" class="indexterm-anchor"></a>OLAP Aggregate Function Calc
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5890 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5890 d2274789e223 ">
                              <p>The number of times the <code class="codeph">AGGREGATE</code> function computes a parent value based on the values of its children.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5890 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5910" headers="d2274789e217 ">
                              <p><a id="d2274789e5912" class="indexterm-anchor"></a>OLAP Aggregate Function Logical NA
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5910 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5910 d2274789e223 ">
                              <p>The number of times an <code class="codeph">AGGREGATE</code> function evaluates to a logical NA value. This could be because the <code class="codeph">AGGINDEX</code> is on and the composite tuple does not exist.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5910 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5933" headers="d2274789e217 ">
                              <p><a id="d2274789e5935" class="indexterm-anchor"></a>OLAP Aggregate Function Precompute
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5933 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5933 d2274789e223 ">
                              <p>The number of times the <code class="codeph">AGGREGATE</code> function is to compute a value and finds it precomputed in the cube.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5933 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5953" headers="d2274789e217 ">
                              <p><a id="d2274789e5955" class="indexterm-anchor"></a>OLAP Custom Member Limit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5953 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5953 d2274789e223 ">
                              <p>The number of times an OLAP table function issues a custom member limit</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5953 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5970" headers="d2274789e217 ">
                              <p><a id="d2274789e5972" class="indexterm-anchor"></a>OLAP Engine Calls
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5970 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5970 d2274789e223 ">
                              <p>The total number of OLAP transactions executed within the session. This value provides a general indication of the level of OLAP activity in the session.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5970 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e5987" headers="d2274789e217 ">
                              <p><a id="d2274789e5989" class="indexterm-anchor"></a>OLAP Fast Limit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e5987 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e5987 d2274789e223 ">
                              <p>The number of times an OLAP table function issues a fast limit</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e5987 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6004" headers="d2274789e217 ">
                              <p><a id="d2274789e6006" class="indexterm-anchor"></a>OLAP Full Limit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6004 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6004 d2274789e223 ">
                              <p>The number of times an OLAP table function issues a full limit</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6004 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6021" headers="d2274789e217 ">
                              <p><a id="d2274789e6023" class="indexterm-anchor"></a>OLAP GID Limit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6021 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6021 d2274789e223 ">
                              <p>The number of times an OLAP table function issues a Cube Grouping ID (CGID) limit. Typically, this type of limit occurs for query rewrite transformations that resolve to a cube organized materialized view.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6021 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6039" headers="d2274789e217 ">
                              <p><a id="d2274789e6041" class="indexterm-anchor"></a>OLAP Import Rows Loaded
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6039 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6039 d2274789e223 ">
                              <p>The number of OLAP import rows loaded. This statistic provides the number of rows of the source cursor that are actually loaded into an Analytic Workspace (AW).</p>
                              <p>The difference between the OLAP Import Rows Pushed and OLAP Import Rows Loaded provides the number of rejected rows.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6039 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6058" headers="d2274789e217 ">
                              <p><a id="d2274789e6060" class="indexterm-anchor"></a>OLAP Import Rows Pushed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6058 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6058 d2274789e223 ">
                              <p>The number of OLAP import rows pushed. This statistic refers to the number of rows encountered from a source cursor and is useful during cube build operations.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6058 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6075" headers="d2274789e217 ">
                              <p><a id="d2274789e6077" class="indexterm-anchor"></a>OLAP INHIER Limit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6075 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6075 d2274789e223 ">
                              <p>The number of times an OLAP table function issues an in-hierarchy limit. This type of limit can occur when you use cube dimension hierarchy views.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6075 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6092" headers="d2274789e217 ">
                              <p><a id="d2274789e6094" class="indexterm-anchor"></a>OLAP Limit Time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6092 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6092 d2274789e223 ">
                              <p>The total time taken by all the OLAP Limit operations that were performed during the last call to the OLAP table function</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6092 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6109" headers="d2274789e217 ">
                              <p><a id="d2274789e6111" class="indexterm-anchor"></a>OLAP Paging Manager Cache Changed Page
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6109 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6109 d2274789e223 ">
                              <p>The number of times the OLAP page pool is changed for any attached AW.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6109 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6126" headers="d2274789e217 ">
                              <p><a id="d2274789e6128" class="indexterm-anchor"></a>OLAP Paging Manager Cache Hit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6126 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6126 d2274789e223 ">
                              <p>The number of times a requested page is found in the OLAP page pool. Use this statistic in conjunction with <a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BABGHHEC">OLAP Paging Manager Cache Miss</a> to determine the OLAP page pool efficiency ratio.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6126 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6146" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__BABGHHEC"><a id="d2274789e6148" class="indexterm-anchor"></a>OLAP Paging Manager Cache Miss
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6146 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6146 d2274789e223 ">
                              <p>The number of times a requested page is not found in the OLAP page pool. Use this statistic in conjunction with OLAP Paging Manager Cache Hit to determine the OLAP page pool efficiency ratio.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6146 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6163" headers="d2274789e217 ">
                              <p><a id="d2274789e6165" class="indexterm-anchor"></a>OLAP Paging Manager Cache Write
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6163 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6163 d2274789e223 ">
                              <p>The number of times the OLAP paging manager writes to a page in the OLAP page pool.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6163 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6180" headers="d2274789e217 ">
                              <p><a id="d2274789e6182" class="indexterm-anchor"></a>OLAP Paging Manager New Page
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6180 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6180 d2274789e223 ">
                              <p>The number of newly-created pages in the OLAP page pool that have not yet been written to the workspace LOB</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6180 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6197" headers="d2274789e217 ">
                              <p><a id="d2274789e6199" class="indexterm-anchor"></a>OLAP Paging Manager Pool Size
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6197 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6197 d2274789e223 ">
                              <p>Size, in bytes, of the OLAP page pool allocated to a session and the sum of all OLAP page pools in the system.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6197 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6214" headers="d2274789e217 ">
                              <p><a id="d2274789e6216" class="indexterm-anchor"></a>OLAP Perm LOB Read
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6214 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6214 d2274789e223 ">
                              <p>The number of times data was read from the table where the AW is stored. These are permanent LOB reads.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6214 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6232" headers="d2274789e217 ">
                              <p><a id="d2274789e6234" class="indexterm-anchor"></a>OLAP Row Id Limit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6232 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6232 d2274789e223 ">
                              <p>The number of times an OLAP table function issues a row Id limit.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6232 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6249" headers="d2274789e217 ">
                              <p><a id="d2274789e6251" class="indexterm-anchor"></a>OLAP Row Load Time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6249 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6249 d2274789e223 ">
                              <p>The total time spent loading rows into an AW during cube build and OLAP SQL import operations.</p>
                              <p>Use this statistic along with the <a href="V-SESS_TIME_MODEL.html#GUID-B5CF4362-325D-4F22-9A08-0873FA32A5C0__CHDJBEDH">OLAP engine elapsed time</a> to measure time spent running OLAP engine routines that involve loading data into AWs from a SQL source.
                              </p>
                              <p>This statistic has the following levels of precision:</p>
                              <ul style="list-style-type: disc;">
                                 <li>
                                    <p>Low precision timer</p>
                                    <p>This captures the elapsed time of the entire fetch phase of the SQL cursor that is being loaded into AWs. It includes the SQL execution time that occurs during a fetch operation from a source cursor and time taken by the OLAP engine to populate AWs.</p>
                                 </li>
                                 <li>
                                    <p>High precision timer</p>
                                    <p>This captures the elapsed time, excluding the SQL processing of the cursor being loaded. It records the time spent in the OLAP engine only.</p>
                                 </li>
                                 <li>
                                    <p>Default timer precision:</p>
                                    <p>This is based on the <code class="codeph">STATISTIC_LEVEL</code> parameter. If the low precision is used, then <code class="codeph">STATISTICS_LEVEL</code> is TYPICAL. The high precision timer is used when <code class="codeph">STATISTIC_LEVEL</code> is set to ALL. No timing is captured when <code class="codeph">STATISTICS_LEVEL</code> is BASIC.
                                    </p>
                                 </li>
                              </ul>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6249 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6301" headers="d2274789e217 ">
                              <p><a id="d2274789e6303" class="indexterm-anchor"></a>OLAP Row Source Rows Processed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6301 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6301 d2274789e223 ">
                              <p>The number of rows processed by the OLAP row source</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6301 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6318" headers="d2274789e217 ">
                              <p><a id="d2274789e6320" class="indexterm-anchor"></a>OLAP Session Cache Hit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6318 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6318 d2274789e223 ">
                              <p>The number of times the requested, dynamically-aggregated value of an AW object, was found in the OLAP session cache.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6318 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6335" headers="d2274789e217 ">
                              <p><a id="d2274789e6337" class="indexterm-anchor"></a>OLAP Session Cache Miss
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6335 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6335 d2274789e223 ">
                              <p>The number of times the requested, dynamically-aggregated value of an AW object, was not found in the OLAP session cache.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6335 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6352" headers="d2274789e217 ">
                              <p><a id="d2274789e6354" class="indexterm-anchor"></a>OLAP Temp Segment Read
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6352 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6352 d2274789e223 ">
                              <p>The number of times data was read from a temporary segment and not from the OLAP page pool</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6352 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6369" headers="d2274789e217 ">
                              <p><a id="d2274789e6371" class="indexterm-anchor"></a>OLAP Temp Segments
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6369 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6369 d2274789e223 ">
                              <p>The number of OLAP pages stored in temporary segments for analytic workspaces</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6369 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6386" headers="d2274789e217 ">
                              <p><a id="d2274789e6388" class="indexterm-anchor"></a>OLAP Unique Key Attribute Limit
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6386 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6386 d2274789e223 ">
                              <p>The number of times an OLAP table function issues a unique key attribute limit</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6386 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6403" headers="d2274789e217 ">
                              <p><a id="d2274789e6405" class="indexterm-anchor"></a>opened cursors cumulative
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6403 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6403 d2274789e223 ">
                              <p>In V$SYSSTAT: Total number of cursors opened since the instance started.</p>
                              <p>In V$SESSTAT: Total number of cursors opened since the start of the session.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6403 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6422" headers="d2274789e217 ">
                              <p><a id="d2274789e6424" class="indexterm-anchor"></a>opened cursors current
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6422 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6422 d2274789e223 ">
                              <p>Total number of current open cursors</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6422 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6439" headers="d2274789e217 ">
                              <p><a id="d2274789e6441" class="indexterm-anchor"></a>OS CPU Qt wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6439 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6439 d2274789e223 ">
                              <p>The time a session spends on the CPU run queue (in microseconds), waiting to get the CPU to run</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6439 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6459" headers="d2274789e217 ">
                              <p><a id="d2274789e6461" class="indexterm-anchor"></a>OS Involuntary context switches
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6459 d2274789e220 ">
                              <p>16</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6459 d2274789e223 ">
                              <p>Number of context switches that were enforced by the operating system</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6459 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6478" headers="d2274789e217 ">
                              <p><a id="d2274789e6480" class="indexterm-anchor"></a>OS Signals received
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6478 d2274789e220 ">
                              <p>16</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6478 d2274789e223 ">
                              <p>Number of signals received</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6478 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6497" headers="d2274789e217 ">
                              <p><a id="d2274789e6499" class="indexterm-anchor"></a>OS Swaps
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6497 d2274789e220 ">
                              <p>16</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6497 d2274789e223 ">
                              <p>Number of swap pages</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6497 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6516" headers="d2274789e217 ">
                              <p><a id="d2274789e6518" class="indexterm-anchor"></a>OS Voluntary context switches
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6516 d2274789e220 ">
                              <p>16</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6516 d2274789e223 ">
                              <p>Number of voluntary context switches (for example, when a process gives up the CPU by a SLEEP() system call)</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6516 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6535" headers="d2274789e217 ">
                              <p><a id="d2274789e6537" class="indexterm-anchor"></a>Parallel operations downgraded 1 to 25 pct
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6535 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6535 d2274789e223 ">
                              <p>Number of times parallel execution was requested and the degree of parallelism was reduced because of insufficient parallel execution servers</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6535 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6552" headers="d2274789e217 ">
                              <p><a id="d2274789e6554" class="indexterm-anchor"></a>Parallel operations downgraded 25 to 50 pct
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6552 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6552 d2274789e223 ">
                              <p>Number of times parallel execution was requested and the degree of parallelism was reduced because of insufficient parallel execution servers</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6552 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6569" headers="d2274789e217 ">
                              <p><a id="d2274789e6571" class="indexterm-anchor"></a>Parallel operations downgraded 50 to 75 pct
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6569 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6569 d2274789e223 ">
                              <p>Number of times parallel execution was requested and the degree of parallelism was reduced because of insufficient parallel execution servers</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6569 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6586" headers="d2274789e217 ">
                              <p><a id="d2274789e6588" class="indexterm-anchor"></a>Parallel operations downgraded 75 to 99 pct
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6586 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6586 d2274789e223 ">
                              <p>Number of times parallel execution was requested and the degree of parallelism was reduced because of insufficient parallel execution servers</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6586 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6603" headers="d2274789e217 ">
                              <p><a id="d2274789e6605" class="indexterm-anchor"></a>Parallel operations downgraded to serial
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6603 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6603 d2274789e223 ">
                              <p>Number of times parallel execution was requested but execution was serial because of insufficient parallel execution servers</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6603 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6620" headers="d2274789e217 ">
                              <p><a id="d2274789e6622" class="indexterm-anchor"></a>Parallel operations not downgraded
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6620 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6620 d2274789e223 ">
                              <p>Number of times parallel execution was executed at the requested degree of parallelism</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6620 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6637" headers="d2274789e217 ">
                              <p><a id="d2274789e6639" class="indexterm-anchor"></a>parse count (describe)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6637 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6637 d2274789e223 ">
                              <p>Total number of parse calls on a describe cursor. This operation is a less expensive than a hard parse and more expensive than a soft parse.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6637 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6655" headers="d2274789e217 ">
                              <p><a id="d2274789e6657" class="indexterm-anchor"></a>parse count (hard)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6655 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6655 d2274789e223 ">
                              <p>Total number of parse calls (real parses). A hard parse is a very expensive operation in terms of memory use, because it requires Oracle to allocate a workheap and other memory structures and then build a parse tree.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6655 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6672" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26932"><a id="d2274789e6674" class="indexterm-anchor"></a>parse count (total)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6672 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6672 d2274789e223 ">
                              <p>Total number of parse calls (hard, soft, and describe). A soft parse is a check on an object already in the shared pool, to verify that the permissions on the underlying object have not changed.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6672 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6689" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26940"><a id="d2274789e6691" class="indexterm-anchor"></a>parse time cpu
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6689 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6689 d2274789e223 ">
                              <p>Total CPU time used for parsing (hard and soft) in 10s of milliseconds</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6689 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6706" headers="d2274789e217 ">
                              <p><a id="d2274789e6708" class="indexterm-anchor"></a>parse time elapsed
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6706 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6706 d2274789e223 ">
                              <p>Total elapsed time for parsing, in 10s of milliseconds. Subtract <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26940">parse time cpu</a>"</span> from this statistic to determine the total waiting time for parse resources.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6706 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6727" headers="d2274789e217 ">
                              <p><a id="d2274789e6729" class="indexterm-anchor"></a>physical read bytes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6727 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6727 d2274789e223 ">
                              <p>Total size in bytes of all disk reads by application activity (and not other instance activity) only.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6727 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6744" headers="d2274789e217 ">
                              <p><a id="d2274789e6746" class="indexterm-anchor"></a>physical read flash cache hits
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6744 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6744 d2274789e223 ">
                              <p>Total number of reads from flash cache instead of disk</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6744 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6761" headers="d2274789e217 ">
                              <p><a id="d2274789e6763" class="indexterm-anchor"></a>physical read IO requests
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6761 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6761 d2274789e223 ">
                              <p>Number of read requests for application activity (mainly buffer cache and direct load operation) which read one or more database blocks per request. This is a subset of "physical read total IO requests" statistic.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6761 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6778" headers="d2274789e217 ">
                              <p><a id="d2274789e6780" class="indexterm-anchor"></a>physical read requests optimized
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6778 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6778 d2274789e223 ">
                              <p>Number of read requests that read one or more database blocks from the Database Smart Flash Cache or the Exadata Smart Flash Cache.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6778 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6795" headers="d2274789e217 ">
                              <p><a id="d2274789e6797" class="indexterm-anchor"></a>physical read total bytes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6795 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6795 d2274789e223 ">
                              <p>Total size in bytes of disk reads by all database instance activity including application reads, backup and recovery, and other utilities. The difference between this value and "physical read bytes" gives the total read size in bytes by non-application workload.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6795 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6812" headers="d2274789e217 ">
                              <p><a id="d2274789e6814" class="indexterm-anchor"></a>physical read total IO requests
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6812 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6812 d2274789e223 ">
                              <p>Number of read requests which read one or more database blocks for all instance activity including application, backup and recovery, and other utilities.</p>
                              <p> The difference between this value and "physical read total multi block requests" gives the total number of small I/O requests which are less than 128 kilobytes down to single block read requests.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6812 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6831" headers="d2274789e217 ">
                              <p><a id="d2274789e6833" class="indexterm-anchor"></a>physical read total multi block requests
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6831 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6831 d2274789e223 ">
                              <p>Total number of Oracle instance read requests which read 128 kilobytes or more in two or more database blocks per request for all instance activity including application, backup and recovery, and other utilities.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6831 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6849" headers="d2274789e217 ">
                              <p><a id="d2274789e6851" class="indexterm-anchor"></a>physical reads
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6849 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6849 d2274789e223 ">
                              <p>Total number of data blocks read from disk. This value can be greater than the value of "physical reads direct" plus "physical reads cache" as reads into process private buffers also included in this statistic.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6849 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6866" headers="d2274789e217 ">
                              <p><a id="d2274789e6868" class="indexterm-anchor"></a>physical reads cache
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6866 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6866 d2274789e223 ">
                              <p>Total number of data blocks read from disk into the buffer cache. This is a subset of "physical reads" statistic.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6866 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6883" headers="d2274789e217 ">
                              <p><a id="d2274789e6885" class="indexterm-anchor"></a>physical reads cache prefetch
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6883 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6883 d2274789e223 ">
                              <p>Number of contiguous and noncontiguous blocks that were prefetched.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6883 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6900" headers="d2274789e217 ">
                              <p><a id="d2274789e6902" class="indexterm-anchor"></a>physical reads direct
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6900 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6900 d2274789e223 ">
                              <p>Number of reads directly from disk, bypassing the buffer cache. For example, in high bandwidth, data-intensive operations such as parallel query, reads of disk blocks bypass the buffer cache to maximize transfer rates and to prevent the premature aging of shared data blocks resident in the buffer cache.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6900 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6917" headers="d2274789e217 ">
                              <p><a id="d2274789e6919" class="indexterm-anchor"></a>physical reads direct (lob)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6917 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6917 d2274789e223 ">
                              <p>Number of buffers that were read directly for LOBs</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6917 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6934" headers="d2274789e217 ">
                              <p><a id="d2274789e6936" class="indexterm-anchor"></a>physical reads direct temporary tablespace
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6934 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6934 d2274789e223 ">
                              <p>Number of buffers that were read directly from temporary tablespaces</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6934 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6951" headers="d2274789e217 ">
                              <p><a id="d2274789e6953" class="indexterm-anchor"></a>physical reads for flashback new
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6951 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6951 d2274789e223 ">
                              <p>Number of blocks read for newing (that is, preparing a data block for a completely new change) blocks while flashback database is enabled</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6951 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6968" headers="d2274789e217 ">
                              <p><a id="d2274789e6970" class="indexterm-anchor"></a>physical reads prefetch warmup
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6968 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6968 d2274789e223 ">
                              <p>Number of data blocks that were read from the disk during the automatic prewarming of the buffer cache.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6968 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e6985" headers="d2274789e217 ">
                              <p><a id="d2274789e6987" class="indexterm-anchor"></a>physical write bytes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e6985 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e6985 d2274789e223 ">
                              <p>Total size in bytes of all disk writes from the database application activity (and not other kinds of instance activity).</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e6985 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7002" headers="d2274789e217 ">
                              <p><a id="d2274789e7004" class="indexterm-anchor"></a>physical write IO requests
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7002 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7002 d2274789e223 ">
                              <p>Number of write requests for application activity (mainly buffer cache and direct load operation) which wrote one or more database blocks per request.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7002 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7019" headers="d2274789e217 ">
                              <p><a id="d2274789e7021" class="indexterm-anchor"></a>physical write total bytes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7019 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7019 d2274789e223 ">
                              <p>Total size in bytes of all disk writes for the database instance including application activity, backup and recovery, and other utilities. The difference between this value and "physical write bytes" gives the total write size in bytes by non-application workload.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7019 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7037" headers="d2274789e217 ">
                              <p><a id="d2274789e7039" class="indexterm-anchor"></a>physical write total IO requests
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7037 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7037 d2274789e223 ">
                              <p>Number of write requests which wrote one or more database blocks from all instance activity including application activity, backup and recovery, and other utilities. The difference between this stat and "physical write total multi block requests" gives the number of single block write requests.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7037 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7054" headers="d2274789e217 ">
                              <p><a id="d2274789e7056" class="indexterm-anchor"></a>physical write total multi block requests
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7054 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7054 d2274789e223 ">
                              <p>Total number of Oracle instance write requests which wrote two or more blocks per request to the disk for all instance activity including application activity, recovery and backup, and other utilities.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7054 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7071" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26976"><a id="d2274789e7073" class="indexterm-anchor"></a>physical writes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7071 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7071 d2274789e223 ">
                              <p>Total number of data blocks written to disk. This statistics value equals the sum of "physical writes direct" and "physical writes from cache" values.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7071 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7088" headers="d2274789e217 ">
                              <p><a id="d2274789e7090" class="indexterm-anchor"></a>physical writes direct
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7088 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7088 d2274789e223 ">
                              <p>Number of writes directly to disk, bypassing the buffer cache (as in a direct load operation)</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7088 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7105" headers="d2274789e217 ">
                              <p><a id="d2274789e7107" class="indexterm-anchor"></a>physical writes direct (lob)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7105 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7105 d2274789e223 ">
                              <p>Number of buffers that were directly written for LOBs</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7105 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7122" headers="d2274789e217 ">
                              <p><a id="d2274789e7124" class="indexterm-anchor"></a>physical writes direct temporary tablespace
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7122 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7122 d2274789e223 ">
                              <p>Number of buffers that were directly written for temporary tablespaces</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7122 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7139" headers="d2274789e217 ">
                              <p><a id="d2274789e7141" class="indexterm-anchor"></a>physical writes from cache
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7139 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7139 d2274789e223 ">
                              <p>Total number of data blocks written to disk from the buffer cache. This is a subset of "physical writes" statistic.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7139 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7156" headers="d2274789e217 ">
                              <p><a id="d2274789e7158" class="indexterm-anchor"></a>physical writes non checkpoint
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7156 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7156 d2274789e223 ">
                              <p>Number of times a buffer is written for reasons other than advancement of the checkpoint. Used as a metric for determining the I/O overhead imposed by setting the <code class="codeph">FAST_START_IO_TARGET</code> parameter to limit recovery I/Os. (Note that <code class="codeph">FAST_START_IO_TARGET</code> is a deprecated parameter.) Essentially this statistic measures the number of writes that would have occurred had there been no checkpointing. Subtracting this value from <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26976">physical writes</a>"</span> gives the extra I/O for checkpointing.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7156 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7183" headers="d2274789e217 ">
                              <p><a id="d2274789e7185" class="indexterm-anchor"></a>pinned buffers inspected
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7183 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7183 d2274789e223 ">
                              <p>Number of times a user process, when scanning the tail of the replacement list looking for a buffer to reuse, encountered a cold buffer that was pinned or had a waiter that was about to pin it. This occurrence is uncommon, because a cold buffer should not be pinned very often.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7183 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7200" headers="d2274789e217 ">
                              <p><a id="d2274789e7202" class="indexterm-anchor"></a>prefetched blocks aged out before use
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7200 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7200 d2274789e223 ">
                              <p>Number of contiguous and noncontiguous blocks that were prefetched but aged out before use</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7200 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7217" headers="d2274789e217 ">
                              <p><a id="d2274789e7219" class="indexterm-anchor"></a>process last non-idle time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7217 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7217 d2274789e223 ">
                              <p>The last time this process executed</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7217 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7235" headers="d2274789e217 ">
                              <p><a id="d2274789e7237" class="indexterm-anchor"></a>PX local messages recv'd
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7235 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7235 d2274789e223 ">
                              <p>Number of local messages received for parallel execution within the instance local to the current session</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7235 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7252" headers="d2274789e217 ">
                              <p><a id="d2274789e7254" class="indexterm-anchor"></a>PX local messages sent
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7252 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7252 d2274789e223 ">
                              <p>Number of local messages sent for parallel execution within the instance local to the current session</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7252 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7269" headers="d2274789e217 ">
                              <p><a id="d2274789e7271" class="indexterm-anchor"></a>PX remote messages recv'd
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7269 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7269 d2274789e223 ">
                              <p>Number of remote messages received for parallel execution within the instance local to the current session</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7269 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7286" headers="d2274789e217 ">
                              <p><a id="d2274789e7288" class="indexterm-anchor"></a>PX remote messages sent
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7286 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7286 d2274789e223 ">
                              <p>Number of remote messages sent for parallel execution within the instance local to the current session</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7286 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7303" headers="d2274789e217 ">
                              <p><a id="d2274789e7305" class="indexterm-anchor"></a>queries parallelized
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7303 d2274789e220 ">
                              <p>32</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7303 d2274789e223 ">
                              <p>Number of SELECT statements executed in parallel</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7303 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7320" headers="d2274789e217 ">
                              <p><a id="d2274789e7322" class="indexterm-anchor"></a>recovery array read time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7320 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7320 d2274789e223 ">
                              <p>Elapsed time of I/O during recovery</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7320 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7337" headers="d2274789e217 ">
                              <p><a id="d2274789e7339" class="indexterm-anchor"></a>recovery array reads
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7337 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7337 d2274789e223 ">
                              <p>Number of reads performed during recovery</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7337 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7354" headers="d2274789e217 ">
                              <p><a id="d2274789e7356" class="indexterm-anchor"></a>recovery blocks read
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7354 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7354 d2274789e223 ">
                              <p>Number of blocks read during recovery</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7354 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7371" headers="d2274789e217 ">
                              <p><a id="d2274789e7373" class="indexterm-anchor"></a>recovery blocks read for lost write detection
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7371 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7371 d2274789e223 ">
                              <p>Number of blocks read for lost write checks during recovery.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7371 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7388" headers="d2274789e217 ">
                              <p><a id="d2274789e7390" class="indexterm-anchor"></a>recovery blocks skipped lost write checks
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7388 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7388 d2274789e223 ">
                              <p>Number of Block Read Records that skipped the lost write check during recovery.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7388 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7405" headers="d2274789e217 ">
                              <p><a id="d2274789e7407" class="indexterm-anchor"></a>recursive calls
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7405 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7405 d2274789e223 ">
                              <p>Number of recursive calls generated at both the user and system level. Oracle maintains tables used for internal processing. When Oracle needs to make a change to these tables, it internally generates an internal SQL statement, which in turn generates a recursive call.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7405 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7423" headers="d2274789e217 ">
                              <p><a id="d2274789e7425" class="indexterm-anchor"></a>recursive cpu usage
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7423 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7423 d2274789e223 ">
                              <p>Total CPU time used by non-user calls (recursive calls). Subtract this value from <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26169">CPU used by this session</a>"</span> to determine how much CPU time was used by the user calls.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7423 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7444" headers="d2274789e217 ">
                              <p><a id="d2274789e7446" class="indexterm-anchor"></a>redo blocks checksummed by FG (exclusive)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7444 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7444 d2274789e223 ">
                              <p>Number of exclusive redo blocks that were checksummed by the generating foreground processes. An exclusive redo block is the one whose entire redo content belongs to a single redo entry.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7444 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7461" headers="d2274789e217 ">
                              <p><a id="d2274789e7463" class="indexterm-anchor"></a>redo blocks checksummed by LGWR
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7461 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7461 d2274789e223 ">
                              <p>Number of redo blocks that were checksummed by the LGWR.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7461 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7478" headers="d2274789e217 ">
                              <p><a id="d2274789e7480" class="indexterm-anchor"></a>redo blocks written
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7478 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7478 d2274789e223 ">
                              <p>Total number of redo blocks written. This statistic divided by <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27232">redo writes</a>"</span> equals number of blocks per write.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7478 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7499" headers="d2274789e217 ">
                              <p><a id="d2274789e7501" class="indexterm-anchor"></a>redo buffer allocation retries
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7499 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7499 d2274789e223 ">
                              <p>Total number of retries necessary to allocate space in the redo buffer. Retries are needed either because the redo writer has fallen behind or because an event such as a log switch is occurring.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7499 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7516" headers="d2274789e217 ">
                              <p><a id="d2274789e7518" class="indexterm-anchor"></a>redo entries
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7516 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7516 d2274789e223 ">
                              <p>Number of times a redo entry is copied into the redo log buffer</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7516 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7533" headers="d2274789e217 ">
                              <p><a id="d2274789e7535" class="indexterm-anchor"></a>redo entries for lost write detection
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7533 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7533 d2274789e223 ">
                              <p>Number of times a Block Read Record is copied into the log buffer.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7533 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7550" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27145"><a id="d2274789e7552" class="indexterm-anchor"></a>redo log space requests
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7550 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7550 d2274789e223 ">
                              <p>Number of times the active log file is full and Oracle must wait for disk space to be allocated for the redo log entries. Such space is created by performing a log switch.</p>
                              <p>Log files that are small in relation to the size of the SGA or the commit rate of the work load can cause problems. When the log switch occurs, Oracle must ensure that all committed dirty buffers are written to disk before switching to a new log file. If you have a large SGA full of dirty buffers and small redo log files, a log switch must wait for DBWR to write dirty buffers to disk before continuing.</p>
                              <p>Also examine the <span class="bold">log file space</span> and <span class="bold">log file space switch</span> wait events in <code class="codeph">V$SESSION_WAIT</code></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7550 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7579" headers="d2274789e217 ">
                              <p><a id="d2274789e7581" class="indexterm-anchor"></a>redo log space wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7579 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7579 d2274789e223 ">
                              <p>Total time waited in centiseconds for available space in the redo log buffer. See also<span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27145">redo log space requests</a>"</span></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7579 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7599" headers="d2274789e217 ">
                              <p><a id="d2274789e7601" class="indexterm-anchor"></a>redo ordering marks
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7599 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7599 d2274789e223 ">
                              <p>Number of times that a system change number was allocated to force a redo record to have a higher SCN than a record generated in another thread using the same block</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7599 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7616" headers="d2274789e217 ">
                              <p><a id="d2274789e7618" class="indexterm-anchor"></a>redo size
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7616 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7616 d2274789e223 ">
                              <p>Total amount of redo generated in bytes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7616 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7634" headers="d2274789e217 ">
                              <p><a id="d2274789e7636" class="indexterm-anchor"></a>redo size for lost write detection
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7634 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7634 d2274789e223 ">
                              <p>Total amount of Block Read Records generated in bytes.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7634 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7651" headers="d2274789e217 ">
                              <p><a id="d2274789e7653" class="indexterm-anchor"></a>redo synch time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7651 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7651 d2274789e223 ">
                              <p>Elapsed time of all <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27197">redo synch writes</a>"</span> calls in 10s of milliseconds
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7651 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7672" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27197"><a id="d2274789e7674" class="indexterm-anchor"></a>redo synch writes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7672 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7672 d2274789e223 ">
                              <p>Number of times the redo is forced to disk, usually for a transaction commit. The log buffer is a circular buffer that LGWR periodically flushes. Usually, redo that is generated and copied into the log buffer need not be flushed out to disk immediately.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7672 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7689" headers="d2274789e217 ">
                              <p><a id="d2274789e7691" class="indexterm-anchor"></a>redo wastage
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7689 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7689 d2274789e223 ">
                              <p>Number of bytes wasted because redo blocks needed to be written before they are completely full. Early writing may be needed to commit transactions, to be able to write a database buffer, or to switch logs.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7689 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7706" headers="d2274789e217 ">
                              <p><a id="d2274789e7708" class="indexterm-anchor"></a>redo write broadcast ack count
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7706 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7706 d2274789e223 ">
                              <p>Number of times a commit broadcast acknowledgment has not been received by the time when the corresponding log write is completed. This is only for Oracle RAC.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7706 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7723" headers="d2274789e217 ">
                              <p><a id="d2274789e7725" class="indexterm-anchor"></a>redo write broadcast ack time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7723 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7723 d2274789e223 ">
                              <p>Total amount of the latency associated with broadcast on commit beyond the latency of the log write (in microseconds). This is only for Oracle RAC.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7723 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7740" headers="d2274789e217 ">
                              <p><a id="d2274789e7742" class="indexterm-anchor"></a>redo write time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7740 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7740 d2274789e223 ">
                              <p>Total elapsed time of the write from the redo log buffer to the current redo log file in 10s of milliseconds</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7740 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7757" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I27232"><a id="d2274789e7759" class="indexterm-anchor"></a>redo writes
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7757 d2274789e220 ">
                              <p>2</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7757 d2274789e223 ">
                              <p>Total number of writes by LGWR to the redo log files. "redo blocks written" divided by this statistic equals the number of blocks per write</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7757 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7774" headers="d2274789e217 ">
                              <p><a id="d2274789e7776" class="indexterm-anchor"></a>rollback changes - undo records applied
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7774 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7774 d2274789e223 ">
                              <p>Number of undo records applied to user-requested rollback changes (not consistent-read rollbacks)</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7774 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7791" headers="d2274789e217 ">
                              <p><a id="d2274789e7793" class="indexterm-anchor"></a>rollbacks only - consistent read gets
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7791 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7791 d2274789e223 ">
                              <p>Number of consistent gets that require only block rollbacks, no block cleanouts.</p>
                              <p><span class="bold">See Also:</span> <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26158">consistent gets</a>"</span> 
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7791 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7816" headers="d2274789e217 ">
                              <p><a id="d2274789e7818" class="indexterm-anchor"></a>rows fetched via callback
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7816 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7816 d2274789e223 ">
                              <p>Rows fetched via callback. Useful primarily for internal debugging purposes.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7816 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7834" headers="d2274789e217 ">
                              <p><a id="d2274789e7836" class="indexterm-anchor"></a>scheduler wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7834 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7834 d2274789e223 ">
                              <p>The total wait time (in microseconds) for waits that belong to the Scheduler wait class</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7834 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7851" headers="d2274789e217 ">
                              <p><a id="d2274789e7853" class="indexterm-anchor"></a>SCN increments due to another database
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7851 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7851 d2274789e223 ">
                              <p>SCN increments due to communication with another database</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7851 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7868" headers="d2274789e217 ">
                              <p><a id="d2274789e7870" class="indexterm-anchor"></a>serializable aborts
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7868 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7868 d2274789e223 ">
                              <p>Number of times a SQL statement in a serializable isolation level had to abort</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7868 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7885" headers="d2274789e217 ">
                              <p><a id="d2274789e7887" class="indexterm-anchor"></a>session connect time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7885 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7885 d2274789e223 ">
                              <p>The connect time for the session in 10s of milliseconds. This value is useful only in <code class="codeph">V$SESSTAT</code>. It is the wall clock time since the logon to this session occurred.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7885 d2274789e226 ">
                              <p>Y</p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7905" headers="d2274789e217 ">
                              <p><a id="d2274789e7907" class="indexterm-anchor"></a>session cursor cache count
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7905 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7905 d2274789e223 ">
                              <p>Total number of cursors cached. This statistic is incremented only if <code class="codeph">SESSION_CACHED_CURSORS </code>&gt; 0. This statistic is the most useful in <code class="codeph">V$SESSTAT</code>. If the value for this statistic in <code class="codeph">V$SESSTAT</code> is close to the setting of the <code class="codeph">SESSION_CACHED_CURSORS</code> parameter, the value of the parameter should be increased.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7905 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7934" headers="d2274789e217 ">
                              <p><a id="d2274789e7936" class="indexterm-anchor"></a>session cursor cache hits
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7934 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7934 d2274789e223 ">
                              <p>Number of hits in the session cursor cache. A hit means that the SQL (including recursive SQL) or PL/SQL statement did not have to be reparsed. Subtract this statistic from <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26932">parse count (total)</a>"</span> to determine the real number of parses that occurred.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7934 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7955" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I28932"><a id="d2274789e7957" class="indexterm-anchor"></a>session logical reads
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7955 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7955 d2274789e223 ">
                              <p>The sum of "db block gets" plus "consistent gets". This includes logical reads of database blocks from either the buffer cache or process private memory.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7955 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7972" headers="d2274789e217 ">
                              <p><a id="d2274789e7974" class="indexterm-anchor"></a>session logical reads - IM
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7972 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7972 d2274789e223 ">
                              <p>Number of database blocks read from the IM column store (number of blocks in IMCU - number of blocks with invalid rows)</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7972 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e7989" headers="d2274789e217 ">
                              <p><a id="d2274789e7991" class="indexterm-anchor"></a>session pga memory
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e7989 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e7989 d2274789e223 ">
                              <p>Current PGA size for the session. Useful only in <code class="codeph">V$SESSTAT</code>; it has no meaning in <code class="codeph">V$SYSSTAT</code>.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e7989 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8012" headers="d2274789e217 ">
                              <p><a id="d2274789e8014" class="indexterm-anchor"></a>session pga memory max
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8012 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8012 d2274789e223 ">
                              <p>Peak PGA size for the session. Useful only in <code class="codeph">V$SESSTAT</code>; it has no meaning in <code class="codeph">V$SYSSTAT</code>.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8012 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8035" headers="d2274789e217 ">
                              <p><a id="d2274789e8037" class="indexterm-anchor"></a>session stored procedure space
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8035 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8035 d2274789e223 ">
                              <p>Amount of memory this session is using for stored procedures</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8035 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8053" headers="d2274789e217 ">
                              <p><a id="d2274789e8055" class="indexterm-anchor"></a>session uga memory
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8053 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8053 d2274789e223 ">
                              <p>Current UGA size for the session. Useful only in <code class="codeph">V$SESSTAT</code>; it has no meaning in <code class="codeph">V$SYSSTAT</code>.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8053 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8076" headers="d2274789e217 ">
                              <p><a id="d2274789e8078" class="indexterm-anchor"></a>session uga memory max
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8076 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8076 d2274789e223 ">
                              <p>Peak UGA size for a session. Useful only in <code class="codeph">V$SESSTAT</code>; it has no meaning in <code class="codeph">V$SYSSTAT</code>.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8076 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8099" headers="d2274789e217 ">
                              <p><a id="d2274789e8101" class="indexterm-anchor"></a>shared hash latch upgrades - no wait
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8099 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8099 d2274789e223 ">
                              <p>A shared hash latch upgrade is when a hash latch is upgraded from shared mode to exclusive mode. This statistic displays the number of times the upgrade completed immediately.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8099 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8116" headers="d2274789e217 ">
                              <p><a id="d2274789e8118" class="indexterm-anchor"></a>shared hash latch upgrades - wait
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8116 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8116 d2274789e223 ">
                              <p>A shared hash latch upgrade is when a hash latch is upgraded from shared mode to exclusive mode. This statistics displays the number of times the upgrade did not complete immediately.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8116 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8133" headers="d2274789e217 ">
                              <p><a id="d2274789e8135" class="indexterm-anchor"></a>shared io pool buffer get failure
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8133 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8133 d2274789e223 ">
                              <p>Number of unsuccessful buffer gets from the shared I/O pool from instance startup time.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8133 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8150" headers="d2274789e217 ">
                              <p><a id="d2274789e8152" class="indexterm-anchor"></a>shared io pool buffer get success
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8150 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8150 d2274789e223 ">
                              <p>Number of successful buffer gets from the shared I/O pool from instance startup time.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8150 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8167" headers="d2274789e217 ">
                              <p><a id="d2274789e8169" class="indexterm-anchor"></a>slave propagated tracked transactions
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8167 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8167 d2274789e223 ">
                              <p>Number of transactions modifying tables enabled for flashback data archive which were archived by a slave process</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8167 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8184" headers="d2274789e217 ">
                              <p><a id="d2274789e8186" class="indexterm-anchor"></a>sorts (disk)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8184 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8184 d2274789e223 ">
                              <p>Number of sort operations that required at least one disk write</p>
                              <p>Sorts that require I/O to disk are quite resource intensive. Try increasing the size of the initialization parameter <code class="codeph">SORT_AREA_SIZE</code>. For more information, see <span class="q">"<a href="SORT_AREA_SIZE.html#GUID-A343E04E-B484-4791-8B01-12E182AA00C7" title="SORT_AREA_SIZE specifies (in bytes) the maximum amount of memory Oracle will use for a sort.">SORT_AREA_SIZE</a>"</span>.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8184 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8215" headers="d2274789e217 ">
                              <p><a id="d2274789e8217" class="indexterm-anchor"></a>sorts (memory)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8215 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8215 d2274789e223 ">
                              <p>Number of sort operations that were performed completely in memory and did not require any disk writes</p>
                              <p>You cannot do much better than memory sorts, except maybe no sorts at all. Sorting is usually caused by selection criteria specifications within table join SQL operations.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8215 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8234" headers="d2274789e217 ">
                              <p><a id="d2274789e8236" class="indexterm-anchor"></a>sorts (rows)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8234 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8234 d2274789e223 ">
                              <p>Total number of rows sorted</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8234 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8251" headers="d2274789e217 ">
                              <p><a id="d2274789e8253" class="indexterm-anchor"></a>SQL*Net roundtrips to/from client
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8251 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8251 d2274789e223 ">
                              <p>Total number of Oracle Net Services messages sent to and received from the client</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8251 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8269" headers="d2274789e217 ">
                              <p><a id="d2274789e8271" class="indexterm-anchor"></a>SQL*Net roundtrips to/from dblink
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8269 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8269 d2274789e223 ">
                              <p>Total number of Oracle Net Services messages sent over and received from a database link</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8269 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8286" headers="d2274789e217 ">
                              <p><a id="d2274789e8288" class="indexterm-anchor"></a>summed dirty queue length
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8286 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8286 d2274789e223 ">
                              <p>The sum of the dirty LRU queue length after every write request. Divide by <span class="bold">write requests</span> to get the average queue length after write completion.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8286 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8306" headers="d2274789e217 ">
                              <p><a id="d2274789e8308" class="indexterm-anchor"></a>switch current to new buffer
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8306 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8306 d2274789e223 ">
                              <p>Number of times the CURRENT block moved to a different buffer, leaving a CR block in the original buffer</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8306 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8323" headers="d2274789e217 ">
                              <p><a id="d2274789e8325" class="indexterm-anchor"></a>table fetch by rowid
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8323 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8323 d2274789e223 ">
                              <p>Number of rows that are fetched using a ROWID (usually recovered from an index)</p>
                              <p>This occurrence of table scans usually indicates either non-optimal queries or tables without indexes. Therefore, this statistic should increase as you optimize queries and provide indexes in the application.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8323 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8342" headers="d2274789e217 ">
                              <p><a id="d2274789e8344" class="indexterm-anchor"></a>table fetch continued row
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8342 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8342 d2274789e223 ">
                              <p>Number of times a chained or migrated row is encountered during a fetch</p>
                              <p>Retrieving rows that span more than one block increases the logical I/O by a factor that corresponds to the number of blocks than need to be accessed. Exporting and re-importing may eliminate this problem. Evaluate the settings for the storage parameters PCTFREE and PCTUSED. This problem cannot be fixed if rows are larger than database blocks (for example, if the <code class="codeph">LONG</code> data type is used and the rows are extremely large).
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8342 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8364" headers="d2274789e217 ">
                              <p><a id="d2274789e8366" class="indexterm-anchor"></a>table scan blocks gotten
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8364 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8364 d2274789e223 ">
                              <p>During scanning operations, each row is retrieved sequentially by Oracle. This statistic counts the number of blocks encountered during the scan.</p>
                              <p>This statistic tells you the number of database blocks that you had to get from the buffer cache for the purpose of scanning. Compare this value with the value of <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I26158">consistent gets</a>"</span> to determine how much of the consistent read activity can be attributed to scanning.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8364 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8387" headers="d2274789e217 ">
                              <p><a id="d2274789e8389" class="indexterm-anchor"></a>table scan disk IMC fallback
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8387 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8387 d2274789e223 ">
                              <p>Number of rows fetched from the buffer cache because they were not present in the IM column store (in a scan that was otherwise performed in memory)</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8387 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8404" headers="d2274789e217 ">
                              <p><a id="d2274789e8406" class="indexterm-anchor"></a>table scan disk non-IMC rows gotten
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8404 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8404 d2274789e223 ">
                              <p>Number of rows fetched during non-In-Memory scan</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8404 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8421" headers="d2274789e217 ">
                              <p><a id="d2274789e8423" class="indexterm-anchor"></a>table scan rows gotten
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8421 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8421 d2274789e223 ">
                              <p>Number of rows that are processed during scanning operations</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8421 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8438" headers="d2274789e217 ">
                              <p><a id="d2274789e8440" class="indexterm-anchor"></a>table scans (cache partitions)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8438 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8438 d2274789e223 ">
                              <p>Number of range scans performed on tables that have the CACHE option enabled</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8438 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8455" headers="d2274789e217 ">
                              <p><a id="d2274789e8457" class="indexterm-anchor"></a>table scans (direct read)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8455 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8455 d2274789e223 ">
                              <p>Number of table scans performed with direct read (bypassing the buffer cache)</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8455 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8473" headers="d2274789e217 ">
                              <p><a id="d2274789e8475" class="indexterm-anchor"></a>table scans (IM)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8473 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8473 d2274789e223 ">
                              <p>Number of segments / granules scanned using In-Memory</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8473 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8490" headers="d2274789e217 ">
                              <p><a id="d2274789e8492" class="indexterm-anchor"></a>table scans (long tables)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8490 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8490 d2274789e223 ">
                              <p>Long (or conversely short) tables can be defined as tables that do not meet the short table criteria as described in <span class="q">"<a href="statistics-descriptions-2.html#GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I28930">table scans (short tables)</a>"</span></p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8490 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8510" headers="d2274789e217 ">
                              <p><a id="d2274789e8512" class="indexterm-anchor"></a>table scans (rowid ranges)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8510 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8510 d2274789e223 ">
                              <p>During parallel query, the number of table scans conducted with specified ROWID ranges</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8510 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8527" headers="d2274789e217 ">
                              <p id="GUID-2FBC1B7E-9123-41DD-8178-96176260A639__I28930"><a id="d2274789e8529" class="indexterm-anchor"></a>table scans (short tables)
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8527 d2274789e220 ">
                              <p>64</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8527 d2274789e223 ">
                              <p>Long (or conversely short) tables can be defined by optimizer hints coming down into the row source access layer of Oracle. The table must have the CACHE option set.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8527 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8544" headers="d2274789e217 ">
                              <p><a id="d2274789e8546" class="indexterm-anchor"></a>tracked rows
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8544 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8544 d2274789e223 ">
                              <p>Number of rows modified in tables enabled for flashback data archive</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8544 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8561" headers="d2274789e217 ">
                              <p><a id="d2274789e8563" class="indexterm-anchor"></a>tracked transactions
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8561 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8561 d2274789e223 ">
                              <p>Number of transactions which modified a table enabled for flashback data archive</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8561 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8578" headers="d2274789e217 ">
                              <p><a id="d2274789e8580" class="indexterm-anchor"></a>transaction lock background get time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8578 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8578 d2274789e223 ">
                              <p>Useful only for internal debugging purposes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8578 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8595" headers="d2274789e217 ">
                              <p><a id="d2274789e8597" class="indexterm-anchor"></a>transaction lock background gets
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8595 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8595 d2274789e223 ">
                              <p>Useful only for internal debugging purposes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8595 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8612" headers="d2274789e217 ">
                              <p><a id="d2274789e8614" class="indexterm-anchor"></a>transaction lock foreground requests
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8612 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8612 d2274789e223 ">
                              <p>Useful only for internal debugging purposes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8612 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8629" headers="d2274789e217 ">
                              <p><a id="d2274789e8631" class="indexterm-anchor"></a>transaction lock foreground wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8629 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8629 d2274789e223 ">
                              <p>Useful only for internal debugging purposes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8629 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8646" headers="d2274789e217 ">
                              <p><a id="d2274789e8648" class="indexterm-anchor"></a>transaction rollbacks
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8646 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8646 d2274789e223 ">
                              <p>Number of transactions being successfully rolled back</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8646 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8664" headers="d2274789e217 ">
                              <p><a id="d2274789e8666" class="indexterm-anchor"></a>transaction tables consistent read rollbacks
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8664 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8664 d2274789e223 ">
                              <p>Number of times rollback segment headers are rolled back to create consistent read blocks</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8664 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8681" headers="d2274789e217 ">
                              <p><a id="d2274789e8683" class="indexterm-anchor"></a>transaction tables consistent reads - undo records applied
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8681 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8681 d2274789e223 ">
                              <p>Number of undo records applied to transaction tables that have been rolled back for consistent read purposes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8681 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8698" headers="d2274789e217 ">
                              <p><a id="d2274789e8700" class="indexterm-anchor"></a>user calls
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8698 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8698 d2274789e223 ">
                              <p>Number of user calls such as login, parse, fetch, or execute</p>
                              <p>When determining activity, the ratio of user calls to RPI calls, give you an indication of how much internal work gets generated because of the type of requests the user is sending to Oracle.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8698 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8717" headers="d2274789e217 ">
                              <p><a id="d2274789e8719" class="indexterm-anchor"></a>user commits
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8717 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8717 d2274789e223 ">
                              <p>Number of user commits. When a user commits a transaction, the redo generated that reflects the changes made to database blocks must be written to disk. Commits often represent the closest thing to a user transaction rate.</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8717 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8734" headers="d2274789e217 ">
                              <p><a id="d2274789e8736" class="indexterm-anchor"></a>user I/O wait time
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8734 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8734 d2274789e223 ">
                              <p>The total wait time (in centiseconds) for waits that belong to the User I/O wait class</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8734 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8751" headers="d2274789e217 ">
                              <p><a id="d2274789e8753" class="indexterm-anchor"></a>user rollbacks
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8751 d2274789e220 ">
                              <p>1</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8751 d2274789e223 ">
                              <p>Number of times users manually issue the <code class="codeph">ROLLBACK</code> statement or an error occurs during a user's transactions
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8751 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8771" headers="d2274789e217 ">
                              <p><a id="d2274789e8773" class="indexterm-anchor"></a>very large tracked transactions
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8771 d2274789e220 ">
                              <p>128</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8771 d2274789e223 ">
                              <p>For tables tracked by flashback data archive, number of transactions modifying those tables which are very large in terms of size or number of changes</p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8771 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8788" headers="d2274789e217 ">
                              <p><a id="d2274789e8790" class="indexterm-anchor"></a>write clones created in background
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8788 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8788 d2274789e223 ">
                              <p>Number of times a background or foreground process clones a <code class="codeph">CURRENT</code> buffer that is being written. The clone becomes the new, accessible <code class="codeph">CURRENT</code> buffer, leaving the original buffer (now the clone) to complete writing.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8788 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                        <tr align="left" valign="top">
                           <td align="left" valign="top" width="28%" id="d2274789e8811" headers="d2274789e217 ">
                              <p><a id="d2274789e8813" class="indexterm-anchor"></a>write clones created in foreground
                              </p>
                           </td>
                           <td align="left" valign="top" width="8%" headers="d2274789e8811 d2274789e220 ">
                              <p>8</p>
                           </td>
                           <td align="left" valign="top" width="51%" headers="d2274789e8811 d2274789e223 ">
                              <p>Number of times a background or foreground process clones a <code class="codeph">CURRENT</code> buffer that is being written. The clone becomes the new, accessible <code class="codeph">CURRENT</code> buffer, leaving the original buffer (now the clone) to complete writing.
                              </p>
                           </td>
                           <td align="left" valign="top" width="14%" headers="d2274789e8811 d2274789e226 ">
                              <p> </p>
                           </td>
                        </tr>
                     </tbody>
                  </table>
