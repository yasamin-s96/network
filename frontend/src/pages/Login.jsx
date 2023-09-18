import Container from "../components/shared/Container"
import AuthCard from "../components/shared/AuthCard"
import AuthButton from "../components/shared/AuthButton"
import SiteDescription from "../components/shared/SiteDescription"
import { Helmet } from "react-helmet"

const Login = () => {
    return (
        <>
            <Helmet>
                <title>Login to Network</title>
            </Helmet>
            <Container additionalClasses="flex justify-between">
                <SiteDescription />
                <AuthCard>
                    <form className="flex flex-col items-center justify-center space-y-4 mb-2">
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="text" placeholder="Username" />
                        <input className="w-full py-2 focus:outline-none rounded-md border border-stone-200 px-2 focus:ring-2" type="password" placeholder="Password" />
                        <AuthButton>Sign in</AuthButton>
                    </form>
                    <p className="text-sm text-slate-500">New to Network?</p>
                    <a className="inline-block text-sm text-indigo-400 hover:text-indigo-500 hover:underline hover:decoration-indigo-500" href="#">Sign up</a>
                </AuthCard>
            </Container>
        </>

    )
}

export default Login