/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext, useEffect, useState } from "react"
import { ColorModeContext, EventLoopContext } from "$/utils/context"
import { Event, getBackendURL, isTrue, refs } from "$/utils/state"
import { MoonIcon as LucideMoonIcon, SunIcon as LucideSunIcon, WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { keyframes } from "@emotion/react"
import { toast, Toaster } from "sonner"
import env from "$/env.json"
import { Button as RadixThemesButton, Card as RadixThemesCard, Container as RadixThemesContainer, Flex as RadixThemesFlex, Grid as RadixThemesGrid, IconButton as RadixThemesIconButton, Popover as RadixThemesPopover, TextField as RadixThemesTextField } from "@radix-ui/themes"
import NextHead from "next/head"



export function Fragment_9017984ada32ffa55f5d2870ebd3c887 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <Fragment>

{isTrue((connectErrors.length > 0)) ? (
  <Fragment>

<LucideWifiOffIcon css={({ ["color"] : "crimson", ["zIndex"] : 9999, ["position"] : "fixed", ["bottom"] : "33px", ["right"] : "33px", ["animation"] : (pulse+" 1s infinite") })} size={32}/>
</Fragment>
) : (
  <Fragment/>
)}
</Fragment>
  )
}

export function Iconbutton_5d4a20c282d066f2f46dc5923d99db7b () {
  const { toggleColorMode } = useContext(ColorModeContext)
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_9922dd3e837b9e087c86a2522c2c93f8 = useCallback(toggleColorMode, [addEvents, Event, toggleColorMode])


  return (
    <RadixThemesIconButton css={({ ["padding"] : "6px", ["position"] : "fixed", ["top"] : "2rem", ["right"] : "2rem", ["background"] : "transparent", ["color"] : "inherit", ["zIndex"] : "20", ["&:hover"] : ({ ["cursor"] : "pointer" }) })} onClick={on_click_9922dd3e837b9e087c86a2522c2c93f8}>

<Fragment_ce8bcea548e7072af157110c53ab895c/>
</RadixThemesIconButton>
  )
}

export function Div_bd4c022a8f796682aa6392e9d4c102e9 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);



  return (
    <div css={({ ["position"] : "fixed", ["width"] : "100vw", ["height"] : "0" })} title={("Connection Error: "+((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : ''))}>

<Fragment_9017984ada32ffa55f5d2870ebd3c887/>
</div>
  )
}

export function Fragment_ce8bcea548e7072af157110c53ab895c () {
  const { resolvedColorMode } = useContext(ColorModeContext)



  return (
    <Fragment>

{isTrue((resolvedColorMode === "light")) ? (
  <Fragment>

<LucideSunIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
) : (
  <Fragment>

<LucideMoonIcon css={({ ["color"] : "var(--current-color)" })}/>
</Fragment>
)}
</Fragment>
  )
}

export function Toaster_6e6ebf8d7ce589d59b7d382fb7576edf () {
  const { resolvedColorMode } = useContext(ColorModeContext)


  refs['__toast'] = toast
  const [addEvents, connectErrors] = useContext(EventLoopContext);
  const toast_props = ({ ["description"] : ("Check if server is reachable at "+getBackendURL(env.EVENT).href), ["closeButton"] : true, ["duration"] : 120000, ["id"] : "websocket-error" });
  const [userDismissed, setUserDismissed] = useState(false);
  (useEffect(
() => {
    if ((connectErrors.length >= 2)) {
        if (!userDismissed) {
            toast.error(
                `Cannot connect to server: ${((connectErrors.length > 0) ? connectErrors[connectErrors.length - 1].message : '')}.`,
                {...toast_props, onDismiss: () => setUserDismissed(true)},
            )
        }
    } else {
        toast.dismiss("websocket-error");
        setUserDismissed(false);  // after reconnection reset dismissed state
    }
}
, [connectErrors]))

  return (
    <Toaster closeButton={false} expand={true} position={"bottom-right"} richColors={true} theme={resolvedColorMode}/>
  )
}

const pulse = keyframes`
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
`


export default function Component() {

  return (
    <Fragment>

<Fragment>

<Div_bd4c022a8f796682aa6392e9d4c102e9/>
<Toaster_6e6ebf8d7ce589d59b7d382fb7576edf/>
</Fragment>
<RadixThemesContainer css={({ ["padding"] : "16px" })} size={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<Iconbutton_5d4a20c282d066f2f46dc5923d99db7b/>
<RadixThemesGrid align={"center"} columns={"8"} css={({ ["size"] : "20", ["width"] : "100%" })} gap={"4"}>

<RadixThemesCard>

{"Alex"}
<img src={"Alex.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Alfred"}
<img src={"Alfred.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Anita"}
<img src={"Anita.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Anne"}
<img src={"Anne.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Bernard"}
<img src={"Bernard.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Bill"}
<img src={"Bill.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Charles"}
<img src={"Charles.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Claire"}
<img src={"Claire.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"David"}
<img src={"David.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Eric"}
<img src={"Eric.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Frans"}
<img src={"Frans.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"George"}
<img src={"George.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Herman"}
<img src={"Herman.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Joe"}
<img src={"Joe.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Maria"}
<img src={"Maria.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Max"}
<img src={"Max.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Paul"}
<img src={"Paul.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Peter"}
<img src={"Peter.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Philip"}
<img src={"Philip.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Richard"}
<img src={"Richard.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Robert"}
<img src={"Robert.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Sam"}
<img src={"Sam.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Susan"}
<img src={"Susan.png"}/>
</RadixThemesCard>
<RadixThemesCard>

{"Tom"}
<img src={"Tom.png"}/>
</RadixThemesCard>
</RadixThemesGrid>
<RadixThemesFlex align={"center"} className={"rx-Stack"} direction={"row"} gap={"3"}>

<RadixThemesTextField.Root placeholder={"Haz una pregunta"}/>
<RadixThemesButton>

{"Enviar"}
</RadixThemesButton>
</RadixThemesFlex>
<RadixThemesPopover.Root>

<RadixThemesPopover.Trigger>

<RadixThemesButton>

{"Respuesta"}
</RadixThemesButton>
</RadixThemesPopover.Trigger>
<RadixThemesPopover.Content>

<RadixThemesFlex direction={"column"} gap={"3"}>

<img css={({ ["size"] : "20" })} src={"Alex.png"}/>
<RadixThemesPopover.Close>

<RadixThemesButton>

{"Close"}
</RadixThemesButton>
</RadixThemesPopover.Close>
</RadixThemesFlex>
</RadixThemesPopover.Content>
</RadixThemesPopover.Root>
</RadixThemesFlex>
</RadixThemesContainer>
<NextHead>

<title>

{"proyecto"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</Fragment>
  )
}
