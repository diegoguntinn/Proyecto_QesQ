/** @jsxImportSource @emotion/react */


import { ErrorBoundary } from "react-error-boundary"
import { Fragment, useCallback, useContext, useEffect, useState } from "react"
import { ColorModeContext, EventLoopContext, StateContexts } from "$/utils/context"
import { Event, getBackendURL, isTrue, refs } from "$/utils/state"
import { jsx, keyframes } from "@emotion/react"
import { MoonIcon as LucideMoonIcon, SunIcon as LucideSunIcon, WifiOffIcon as LucideWifiOffIcon } from "lucide-react"
import { toast, Toaster } from "sonner"
import env from "$/env.json"
import { Box as RadixThemesBox, Button as RadixThemesButton, Card as RadixThemesCard, Container as RadixThemesContainer, Flex as RadixThemesFlex, Grid as RadixThemesGrid, IconButton as RadixThemesIconButton, Popover as RadixThemesPopover, TextField as RadixThemesTextField } from "@radix-ui/themes"
import NextHead from "next/head"



export function Card_07f380532b323194f638034b4184a9fb () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_a330000f3f3bb8838304ecf15cdf520c = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_alex", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_a330000f3f3bb8838304ecf15cdf520c}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Alex"}
</RadixThemesBox>
<Img_70b76e2872c4337c204444b9b6714722/>
</RadixThemesCard>
  )
}

export function Card_0242d99d282cd68e074cb3c8bcd6ead8 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_1bd24ceb0d64258ba656f9c52d16b1bf = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_alfred", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_1bd24ceb0d64258ba656f9c52d16b1bf}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Alfred"}
</RadixThemesBox>
<Img_08efbf82397233d74561ee1421e9f3a2/>
</RadixThemesCard>
  )
}

export function Img_60b1ae80396aec14259ef035f28a75e5 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_richard}/>
  )
}

export function Img_e7d6749187ad9a7f43a51e2242f93b23 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_susan}/>
  )
}

export function Img_e8a138bb5966477fefef25b7e1374991 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_paul}/>
  )
}

export function Img_bc96033e17928814fe15a4df251a442d () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_charles}/>
  )
}

export function Img_43b8798ad4cd02642e425af32bc1f27b () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_max}/>
  )
}

export function Img_70b76e2872c4337c204444b9b6714722 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_alex}/>
  )
}

export function Img_541ae463bf3d8759ab1e56ac478be741 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_maria}/>
  )
}

export function Card_7acb00886815bc0142b32ba7bc9cee63 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_9d0ee9b58aacc7fb06cd6a9629d61dda = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_max", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_9d0ee9b58aacc7fb06cd6a9629d61dda}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Max"}
</RadixThemesBox>
<Img_43b8798ad4cd02642e425af32bc1f27b/>
</RadixThemesCard>
  )
}

export function Card_d19851901b80088c0fc2ca7878c82cb8 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_a986259ebbe6efdfacd51ef0ab56c37b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_peter", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_a986259ebbe6efdfacd51ef0ab56c37b}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Peter"}
</RadixThemesBox>
<Img_b85c01084dc2033a9556d64ce0c49572/>
</RadixThemesCard>
  )
}

export function Img_23632658ca6fcb91b16e857461fbaaf6 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_herman}/>
  )
}

export function Errorboundary_a355f1f6a99a11cb667dac8c1b60d169 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_error_0f5dbf674521530422d73a7946faf6d4 = useCallback(((_error, _info) => (addEvents([(Event("reflex___state____state.reflex___state____frontend_event_exception_state.handle_frontend_exception", ({ ["stack"] : _error["stack"], ["component_stack"] : _info["componentStack"] }), ({  })))], [_error, _info], ({  })))), [addEvents, Event])


  return (
    <ErrorBoundary fallbackRender={((event_args) => (jsx("div", ({ ["css"] : ({ ["height"] : "100%", ["width"] : "100%", ["position"] : "absolute", ["display"] : "flex", ["alignItems"] : "center", ["justifyContent"] : "center" }) }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem" }) }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["flexDirection"] : "column", ["gap"] : "1rem", ["maxWidth"] : "50ch", ["border"] : "1px solid #888888", ["borderRadius"] : "0.25rem", ["padding"] : "1rem" }) }), (jsx("h2", ({ ["css"] : ({ ["fontSize"] : "1.25rem", ["fontWeight"] : "bold" }) }), (jsx(Fragment, ({  }), "An error occurred while rendering this page.")))), (jsx("p", ({ ["css"] : ({ ["opacity"] : "0.75" }) }), (jsx(Fragment, ({  }), "This is an error with the application itself.")))), (jsx("details", ({  }), (jsx("summary", ({ ["css"] : ({ ["padding"] : "0.5rem" }) }), (jsx(Fragment, ({  }), "Error message")))), (jsx("div", ({ ["css"] : ({ ["width"] : "100%", ["maxHeight"] : "50vh", ["overflow"] : "auto", ["background"] : "#000", ["color"] : "#fff", ["borderRadius"] : "0.25rem" }) }), (jsx("div", ({ ["css"] : ({ ["padding"] : "0.5rem", ["width"] : "fit-content" }) }), (jsx("pre", ({  }), (jsx(Fragment, ({  }), event_args.error.stack)))))))), (jsx("button", ({ ["css"] : ({ ["padding"] : "0.35rem 0.75rem", ["margin"] : "0.5rem", ["background"] : "#fff", ["color"] : "#000", ["border"] : "1px solid #000", ["borderRadius"] : "0.25rem", ["fontWeight"] : "bold" }), ["onClick"] : ((...args) => (addEvents([(Event("_call_function", ({ ["function"] : (() => (navigator["clipboard"]["writeText"](event_args.error.stack))) }), ({  })))], args, ({  })))) }), (jsx(Fragment, ({  }), "Copy")))))))), (jsx("hr", ({ ["css"] : ({ ["borderColor"] : "currentColor", ["opacity"] : "0.25" }) }))), (jsx("a", ({ ["href"] : "https://reflex.dev" }), (jsx("div", ({ ["css"] : ({ ["display"] : "flex", ["alignItems"] : "baseline", ["justifyContent"] : "center", ["fontFamily"] : "monospace", ["--default-font-family"] : "monospace", ["gap"] : "0.5rem" }) }), (jsx(Fragment, ({  }), "Built with ")), (jsx("svg", ({ ["css"] : ({ ["viewBox"] : "0 0 56 12", ["fill"] : "currentColor" }), ["height"] : "12", ["width"] : "56", ["xmlns"] : "http://www.w3.org/2000/svg" }), (jsx("path", ({ ["d"] : "M0 11.5999V0.399902H8.96V4.8799H6.72V2.6399H2.24V4.8799H6.72V7.1199H2.24V11.5999H0ZM6.72 11.5999V7.1199H8.96V11.5999H6.72Z" }))), (jsx("path", ({ ["d"] : "M11.2 11.5999V0.399902H17.92V2.6399H13.44V4.8799H17.92V7.1199H13.44V9.3599H17.92V11.5999H11.2Z" }))), (jsx("path", ({ ["d"] : "M20.16 11.5999V0.399902H26.88V2.6399H22.4V4.8799H26.88V7.1199H22.4V11.5999H20.16Z" }))), (jsx("path", ({ ["d"] : "M29.12 11.5999V0.399902H31.36V9.3599H35.84V11.5999H29.12Z" }))), (jsx("path", ({ ["d"] : "M38.08 11.5999V0.399902H44.8V2.6399H40.32V4.8799H44.8V7.1199H40.32V9.3599H44.8V11.5999H38.08Z" }))), (jsx("path", ({ ["d"] : "M47.04 4.8799V0.399902H49.28V4.8799H47.04ZM53.76 4.8799V0.399902H56V4.8799H53.76ZM49.28 7.1199V4.8799H53.76V7.1199H49.28ZM47.04 11.5999V7.1199H49.28V11.5999H47.04ZM53.76 11.5999V7.1199H56V11.5999H53.76Z" }))))))))))))))} onError={on_error_0f5dbf674521530422d73a7946faf6d4}>

<Fragment>

<Div_bd4c022a8f796682aa6392e9d4c102e9/>
<Toaster_6e6ebf8d7ce589d59b7d382fb7576edf/>
</Fragment>
<RadixThemesContainer css={({ ["padding"] : "16px" })} size={"3"}>

<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"column"} gap={"3"}>

<Iconbutton_5d4a20c282d066f2f46dc5923d99db7b/>
<RadixThemesGrid align={"center"} columns={"8"} css={({ ["size"] : "20", ["width"] : "100%" })} gap={"4"}>

<Card_07f380532b323194f638034b4184a9fb/>
<Card_0242d99d282cd68e074cb3c8bcd6ead8/>
<Card_9599eedd2fcf312f28e1ba1153369215/>
<Card_7e81027aba439541258173c9594151f7/>
<Card_1c4f6b70bf00a5b01c7df925e26267ee/>
<Card_b40fe4c0b1414fb1e9f7e8fc8a59a7c3/>
<Card_e025271ad33904c30ab094609cc9dd50/>
<Card_7840a12b6e23ce46a7edfbd5387cbac6/>
<Card_7097410a58e3f5c9cf1c3dbac9e09a56/>
<Card_770bbc913d7a08e242fd9041ec5e2908/>
<Card_b1848495495e2cb42c11f1b65c8510a3/>
<Card_75a29a20322b7193df980aeb0fc6d2dc/>
<Card_81b107ac07f87cb7f4f31ce13af2e021/>
<Card_12ca881ee40362803217bbe912a5cc03/>
<Card_190704d35910afb999755b37feb3cedf/>
<Card_7acb00886815bc0142b32ba7bc9cee63/>
<Card_71c26b6f3071385d0547b90737854d9a/>
<Card_d19851901b80088c0fc2ca7878c82cb8/>
<Card_237950acab51ceb33298087f670dc34d/>
<Card_aa212c01ca85705ecb831cb6edf8e15e/>
<Card_c29d8440051f12639ae0eecd366ebdd3/>
<Card_9bd4454a5413364f66fd8ae22eaae037/>
<Card_81a3def8044fb52ab853df2a9d5a2688/>
<Card_06a31486c9ba80720a65aaabee1af6ba/>
</RadixThemesGrid>
<RadixThemesPopover.Root>

<RadixThemesPopover.Trigger>

<RadixThemesButton>

{"Respuesta"}
</RadixThemesButton>
</RadixThemesPopover.Trigger>
<RadixThemesPopover.Content>

<RadixThemesFlex direction={"column"} gap={"3"}>

<Img_bbdedb9ee352b8f3a9f2b37356898c4b/>
<RadixThemesPopover.Close>

<RadixThemesButton>

{"Cerrar"}
</RadixThemesButton>
</RadixThemesPopover.Close>
</RadixThemesFlex>
</RadixThemesPopover.Content>
</RadixThemesPopover.Root>
<Box_be15224d58e3293baecc415b388039da/>
<RadixThemesFlex align={"start"} className={"rx-Stack"} direction={"row"} gap={"3"}>

<Textfield__root_d1efa397f7b032415f5eb30b52b01dbc/>
<Button_43a2626b6170c04f320c44b0a1daa990/>
</RadixThemesFlex>
</RadixThemesFlex>
</RadixThemesContainer>
<NextHead>

<title>

{"proyecto"}
</title>
<meta content={"favicon.ico"} property={"og:image"}/>
</NextHead>
</ErrorBoundary>
  )
}

export function Img_1ad9c892418bf6678574eed9d18a6689 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_bernard}/>
  )
}

export function Card_aa212c01ca85705ecb831cb6edf8e15e () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_f9255e89bac39baac3adc7ad9f8e4faa = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_richard", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_f9255e89bac39baac3adc7ad9f8e4faa}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Richard"}
</RadixThemesBox>
<Img_60b1ae80396aec14259ef035f28a75e5/>
</RadixThemesCard>
  )
}

export function Img_e7a368befe6ff4f9f81154b9ccfa422a () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_george}/>
  )
}

export function Card_7e81027aba439541258173c9594151f7 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_2f20aacd09f11b62d6d7b811f638069c = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_anne", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_2f20aacd09f11b62d6d7b811f638069c}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Anne"}
</RadixThemesBox>
<Img_0d2569e6b8951a649ad70f4ed0aa156a/>
</RadixThemesCard>
  )
}

export function Card_190704d35910afb999755b37feb3cedf () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_c5943d4cd5696f025c820416c1aefa7b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_maria", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_c5943d4cd5696f025c820416c1aefa7b}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Maria"}
</RadixThemesBox>
<Img_541ae463bf3d8759ab1e56ac478be741/>
</RadixThemesCard>
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


export function Card_71c26b6f3071385d0547b90737854d9a () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_80290ad78694950fcbef211687bc1414 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_paul", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_80290ad78694950fcbef211687bc1414}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Paul"}
</RadixThemesBox>
<Img_e8a138bb5966477fefef25b7e1374991/>
</RadixThemesCard>
  )
}

export function Card_06a31486c9ba80720a65aaabee1af6ba () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_9de48c9ae078dda9b09f3cece8eea22a = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_tom", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_9de48c9ae078dda9b09f3cece8eea22a}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Tom"}
</RadixThemesBox>
<Img_1ab668c6c84805b606515606c7d9373f/>
</RadixThemesCard>
  )
}

export function Card_1c4f6b70bf00a5b01c7df925e26267ee () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_27cd73a7063724b1f9ba13427cc7ec5e = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_bernard", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_27cd73a7063724b1f9ba13427cc7ec5e}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Bernard"}
</RadixThemesBox>
<Img_1ad9c892418bf6678574eed9d18a6689/>
</RadixThemesCard>
  )
}

export function Card_e025271ad33904c30ab094609cc9dd50 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_8e98304219cd0c33d92ed4d137ab2aa8 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_charles", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_8e98304219cd0c33d92ed4d137ab2aa8}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Charles"}
</RadixThemesBox>
<Img_bc96033e17928814fe15a4df251a442d/>
</RadixThemesCard>
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

export function Card_770bbc913d7a08e242fd9041ec5e2908 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_6d1475f18d789b38ea7aeb92f1fb0aab = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_eric", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_6d1475f18d789b38ea7aeb92f1fb0aab}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Eric"}
</RadixThemesBox>
<Img_9a2956f6581eb4cfcf296da22eb48c73/>
</RadixThemesCard>
  )
}

export function Img_b85c01084dc2033a9556d64ce0c49572 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_peter}/>
  )
}

export function Card_9bd4454a5413364f66fd8ae22eaae037 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_3236206a60b882a8b5acd75e39935dc7 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_sam", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_3236206a60b882a8b5acd75e39935dc7}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Sam"}
</RadixThemesBox>
<Img_979604ca3b72f753122d3be8f8d9dd20/>
</RadixThemesCard>
  )
}

export function Button_43a2626b6170c04f320c44b0a1daa990 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_c9b7624522561d1f4b8758c83eca20c7 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___state____state.answer", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesButton css={({ ["backgroundColor"] : "var(--accent-10)", ["boxShadow"] : "rgba(0, 0, 0, 0.15) 0px 2px 8px" })} onClick={on_click_c9b7624522561d1f4b8758c83eca20c7}>

{"Ask"}
</RadixThemesButton>
  )
}

export function Card_9599eedd2fcf312f28e1ba1153369215 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_6947b007196e00116fe92d4b08e88bb2 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_anita", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_6947b007196e00116fe92d4b08e88bb2}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Anita"}
</RadixThemesBox>
<Img_93f3c3b6017dd065c3f95a6d38dfae6f/>
</RadixThemesCard>
  )
}

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

export function Img_93f3c3b6017dd065c3f95a6d38dfae6f () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_anita}/>
  )
}

export function Img_4b08cd1110cddf54cf1d07b527a48c54 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_bill}/>
  )
}

export function Textfield__root_d1efa397f7b032415f5eb30b52b01dbc () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_change_f9a57ed6f06faa64a9e911ac330971db = useCallback(((_e) => (addEvents([(Event("reflex___state____state.proyecto___state____state.set_question", ({ ["value"] : _e["target"]["value"] }), ({  })))], [_e], ({  })))), [addEvents, Event])


  return (
    <RadixThemesTextField.Root css={({ ["borderWidth"] : "1px", ["padding"] : "0.5em", ["boxShadow"] : "rgba(0, 0, 0, 0.15) 0px 2px 8px", ["width"] : "350px" })} onChange={on_change_f9a57ed6f06faa64a9e911ac330971db} placeholder={"Ask a question"}/>
  )
}

export function Img_75226fcd177a86f936885b5404ed3458 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_joe}/>
  )
}

export function Img_1ab668c6c84805b606515606c7d9373f () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_tom}/>
  )
}

export function Card_c29d8440051f12639ae0eecd366ebdd3 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_606fd04987907daa5117ec1d4aaa5441 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_robert", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_606fd04987907daa5117ec1d4aaa5441}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Robert"}
</RadixThemesBox>
<Img_73d717efbbecfecebc44403a1a0fd6b0/>
</RadixThemesCard>
  )
}

export function Img_985a4f59369b28bb4fb8cffdf1e3a00c () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_claire}/>
  )
}

export function Card_81b107ac07f87cb7f4f31ce13af2e021 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_e62320b043a82877aec0ecb50fa0242b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_herman", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_e62320b043a82877aec0ecb50fa0242b}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Herman"}
</RadixThemesBox>
<Img_23632658ca6fcb91b16e857461fbaaf6/>
</RadixThemesCard>
  )
}

export function Img_1e643d66e8204e8483e944a736692aca () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_philip}/>
  )
}

export function Card_81a3def8044fb52ab853df2a9d5a2688 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_cd09940076786554ef8b20a54da881bf = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_susan", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_cd09940076786554ef8b20a54da881bf}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Susan"}
</RadixThemesBox>
<Img_e7d6749187ad9a7f43a51e2242f93b23/>
</RadixThemesCard>
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

export function Img_08efbf82397233d74561ee1421e9f3a2 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_alfred}/>
  )
}

export function Card_75a29a20322b7193df980aeb0fc6d2dc () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_137436cf92de3fcc058c2148d534464b = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_george", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_137436cf92de3fcc058c2148d534464b}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"George"}
</RadixThemesBox>
<Img_e7a368befe6ff4f9f81154b9ccfa422a/>
</RadixThemesCard>
  )
}

export function Card_b1848495495e2cb42c11f1b65c8510a3 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_dcb92b09f58477603b732ee04df3ed8e = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_frans", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_dcb92b09f58477603b732ee04df3ed8e}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Frans"}
</RadixThemesBox>
<Img_70c373d21cbe3e42d23d7b763f1081a7/>
</RadixThemesCard>
  )
}

export function Img_bbdedb9ee352b8f3a9f2b37356898c4b () {
  const reflex___state____state__proyecto___state____state = useContext(StateContexts.reflex___state____state__proyecto___state____state)



  return (
    <img src={(reflex___state____state__proyecto___state____state.personaje_maquina+".png")}/>
  )
}

export function Img_0d2569e6b8951a649ad70f4ed0aa156a () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_anne}/>
  )
}

export function Card_237950acab51ceb33298087f670dc34d () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_ef1bcbbd3c849e7e0fa80b8cce0bdab8 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_philip", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_ef1bcbbd3c849e7e0fa80b8cce0bdab8}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Philip"}
</RadixThemesBox>
<Img_1e643d66e8204e8483e944a736692aca/>
</RadixThemesCard>
  )
}

export function Img_979604ca3b72f753122d3be8f8d9dd20 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_sam}/>
  )
}

export function Img_79af16985227507e1e2dae843047cb89 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_david}/>
  )
}

export function Card_7097410a58e3f5c9cf1c3dbac9e09a56 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_8244045d773ccb0d1294794c60c07942 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_david", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_8244045d773ccb0d1294794c60c07942}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"David"}
</RadixThemesBox>
<Img_79af16985227507e1e2dae843047cb89/>
</RadixThemesCard>
  )
}

export function Card_7840a12b6e23ce46a7edfbd5387cbac6 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_aa0d2d3a56f690e3eeb9523ddce010b4 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_claire", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_aa0d2d3a56f690e3eeb9523ddce010b4}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Claire"}
</RadixThemesBox>
<Img_985a4f59369b28bb4fb8cffdf1e3a00c/>
</RadixThemesCard>
  )
}

export function Card_12ca881ee40362803217bbe912a5cc03 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_7a358c4015b854eda9e79b7a683bb96f = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_joe", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_7a358c4015b854eda9e79b7a683bb96f}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Joe"}
</RadixThemesBox>
<Img_75226fcd177a86f936885b5404ed3458/>
</RadixThemesCard>
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

export function Img_73d717efbbecfecebc44403a1a0fd6b0 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_robert}/>
  )
}

export function Box_be15224d58e3293baecc415b388039da () {
  const reflex___state____state__proyecto___state____state = useContext(StateContexts.reflex___state____state__proyecto___state____state)



  return (
    <RadixThemesBox>

<>{reflex___state____state__proyecto___state____state.chat_history.map((messages, index_54b4eb4f6cf31721) => (
  <RadixThemesBox css={({ ["marginTop"] : "1em", ["marginBottom"] : "1em" })} key={index_54b4eb4f6cf31721}>

<RadixThemesBox css={({ ["textAlign"] : "right" })}>

{messages.at(0)}
</RadixThemesBox>
<RadixThemesBox css={({ ["textAlign"] : "left" })}>

{messages.at(1)}
</RadixThemesBox>
</RadixThemesBox>
))}</>
</RadixThemesBox>
  )
}

export function Card_b40fe4c0b1414fb1e9f7e8fc8a59a7c3 () {
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_click_23f6eb9c8569ab1d694a1002e9b9b750 = useCallback(((...args) => (addEvents([(Event("reflex___state____state.proyecto___proyecto____class_state.toggle_image_bill", ({  }), ({  })))], args, ({  })))), [addEvents, Event])


  return (
    <RadixThemesCard onClick={on_click_23f6eb9c8569ab1d694a1002e9b9b750}>

<RadixThemesBox css={({ ["textAlign"] : "center" })}>

{"Bill"}
</RadixThemesBox>
<Img_4b08cd1110cddf54cf1d07b527a48c54/>
</RadixThemesCard>
  )
}

export function Img_9a2956f6581eb4cfcf296da22eb48c73 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_eric}/>
  )
}

export function Img_70c373d21cbe3e42d23d7b763f1081a7 () {
  const reflex___state____state__proyecto___proyecto____class_state = useContext(StateContexts.reflex___state____state__proyecto___proyecto____class_state)



  return (
    <img src={reflex___state____state__proyecto___proyecto____class_state.img_src_frans}/>
  )
}

export default function Component() {

  return (
    <Errorboundary_a355f1f6a99a11cb667dac8c1b60d169/>
  )
}
