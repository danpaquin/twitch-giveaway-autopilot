# twitch-giveaway-winner
A Twitch bot designed to win chat giveaways

##### Provided under MIT License by Daniel Paquin.
*Note: This script may be subtly broken.  Please use at your own risk.  Get familiar with Twitch's T.O.S. before deploying this script!*
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Benefits
- In about 10 minutes, you could have a script participating in Twitch giveaways for you!
- Please use for educational purposes only!  You should not run this script for extended periods of time.
- Kickstart your own Python IRC Bot!  Change methods how you see fit and create something unique.

## Proof
- Following is a screenshot of me winning a StarCraft Beta Key on my birthday!

![http://imgur.com/zqJtp7d](proof.png)

## Under Development
- Thorough Testing **in progress**

## Getting Started
- Download or clone this repository and place ```TwitchWinner.py``` into your active directory.
- Go to [twitchapps.com/tmi](www.twitchapps.com/tmi/) to get your oauth password

```python
from TwitchWinner import TwitchWinner
bot = TwitchWinner(chan='twitch_channel', nick='your_username', password='oauth_password')
bot.start()
```